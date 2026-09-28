// Run with: node --test tests/player.test.cjs
const assert = require('node:assert/strict');
const { test } = require('node:test');
const { readFileSync } = require('node:fs');
const { runInNewContext } = require('node:vm');
const script = readFileSync(`${__dirname}/../src/barbero_scripts/templates/audio_resume.html`, 'utf8').match(/<script>([\s\S]*?)<\/script>/)[1];

function element(dataset = {}) {
  const handlers = {};
  return {
    dataset, hidden: true, value: '1', textContent: '',
    addEventListener(type, callback) { (handlers[type] ||= []).push(callback); },
    async fire(type) { for (const callback of handlers[type] || []) await callback(); },
    setAttribute(key, value) { this[key] = value; },
    focus() { this.focused = true; },
    select() { this.selected = true; },
  };
}
function storage(values = {}) {
  return {
    getItem: (key) => values[key] ?? null,
    setItem: (key, value) => { values[key] = value; },
    removeItem: (key) => { delete values[key]; },
  };
}
function setup(local = storage(), session = storage()) {
  const ids = Object.fromEntries(['player', 'podcast-audio', 'player-status', 'playback-speed', 'player-title', 'player-close', 'feed-url'].map((id) => [id, element()]));
  ids.player.querySelector = () => element();
  const audio = Object.assign(ids['podcast-audio'], { paused: true, currentTime: 0, duration: 120, ended: false, playCalls: 0 });
  audio.load = () => { audio.currentTime = 0; audio.ended = false; };
  audio.play = async () => { audio.playCalls++; audio.paused = false; await audio.fire('play'); };
  audio.pause = () => { audio.paused = true; void audio.fire('pause'); };
  const buttons = ['one', 'two'].map((slug) => element({ play: slug, title: slug, src: `https://podcast.test/media/${slug}.mp3`, artwork: `https://podcast.test/art/${slug}.webp`, url: `https://podcast.test/episodes/${slug}/` }));
  const copy = element({ copyFeed: 'https://podcast.test/feed.xml' });
  const backLink = element();
  const window = element();
  const classes = new Set();
  runInNewContext(script, {
    document: { getElementById: (id) => ids[id], querySelector: () => backLink, querySelectorAll: (selector) => selector === 'button[data-play]' ? buttons : [copy], body: { classList: { add: (value) => classes.add(value), remove: (value) => classes.delete(value) } } },
    window, localStorage: local, sessionStorage: session, location: { origin: 'https://podcast.test' }, URL, navigator: {}, setTimeout,
  });
  return { ids, audio, buttons, copy, window, classes, backLink };
}

test('single player resumes, switches, remembers selection without autoplay, and closes/reopens', async () => {
  const local = storage({ 'barbero-audio-position:one': '37' });
  const session = storage();
  const page = setup(local, session);
  const { audio, buttons, ids } = page;
  assert.equal(ids.player.hidden, true);
  assert.equal(audio.playCalls, 0);
  await buttons[0].fire('click');
  await audio.fire('loadedmetadata');
  assert.equal(audio.currentTime, 37);
  assert.equal(ids.player.hidden, false);
  assert.equal(buttons[0]['aria-pressed'], 'true');
  audio.currentTime = 45;
  await buttons[1].fire('click');
  assert.equal(local.getItem('barbero-audio-position:one'), '45');
  assert.equal(audio.src, buttons[1].dataset.src);
  await audio.fire('loadedmetadata');
  audio.currentTime = 18;
  await page.window.fire('pagehide');
  assert.equal(local.getItem('barbero-audio-position:two'), '18');
  assert.equal(buttons[0]['aria-pressed'], 'false');
  ids['playback-speed'].value = '1.5';
  await ids['playback-speed'].fire('change');
  assert.equal(audio.playbackRate, 1.5);

  const next = setup(local, session);
  assert.equal(next.ids.player.hidden, false);
  assert.equal(next.audio.src, buttons[1].dataset.src);
  assert.equal(next.audio.playCalls, 0);
  await next.buttons[1].fire('click');
  await next.audio.fire('loadedmetadata');
  assert.equal(next.audio.currentTime, 18);
  next.audio.ended = true;
  next.audio.paused = true;
  await next.audio.fire('ended');
  assert.equal(local.getItem('barbero-audio-position:two'), null);
  await next.ids['player-close'].fire('click');
  assert.equal(next.ids.player.hidden, true);
  assert.equal(session.getItem('barbero-selected-episode'), null);
  assert.equal(next.buttons[1].focused, true);
  await next.buttons[1].fire('click');
  assert.equal(next.ids.player.hidden, false);
  const readingPage = setup(local, session);
  readingPage.buttons.length = 0;
  await readingPage.ids['player-close'].fire('click');
  assert.equal(readingPage.backLink.focused, true);
});

test('blocked storage and clipboard keep controls usable; playback errors are announced', async () => {
  const blocked = { getItem() { throw Error('blocked'); }, setItem() { throw Error('blocked'); }, removeItem() { throw Error('blocked'); } };
  const { audio, buttons, ids, copy } = setup(blocked, blocked);
  await buttons[0].fire('click');
  await audio.fire('loadedmetadata');
  assert.equal(audio.paused, false);
  audio.pause();
  audio.play = async () => { throw Error('unavailable'); };
  await buttons[0].fire('click');
  assert.match(ids['player-status'].textContent, /could not start/);
  await audio.fire('play');
  assert.equal(ids['player-status'].textContent, '');
  await copy.fire('click');
  assert.equal(ids['feed-url'].hidden, false);
  assert.equal(ids['feed-url'].selected, true);
});

test('session data cannot restore an external source', () => {
  const selected = { play: 'one', title: 'one', src: 'https://external.test/audio', artwork: 'https://podcast.test/art', url: 'https://podcast.test/episode' };
  const page = setup(storage(), storage({ 'barbero-selected-episode': JSON.stringify(selected) }));
  assert.equal(page.ids.player.hidden, true);
  assert.equal(page.audio.playCalls, 0);
});
