const wd = require('wd').promiseChainRemote;
const B = require('bluebird');
const app = require('./app');

const TEMPO = 150;
const HIT_HOLD_MS = 15

async function playSong (songStr, elMap) {
  const notes = songStr.split(" ");
  for (const note of notes) {
    if (note.trim() !== "") {
      const [drum, length] = note;
      const duration = (4 / length) * (60 / TEMPO) * 1000;
      await hit(elMap[drum]);
      await B.delay(duration - HIT_HOLD_MS);
    }
  }
}

async function hit (el, delay=HIT_HOLD_MS) {
  await el.sendKeys("0");
  await B.delay(delay);
  await el.sendKeys("1");
}

(async function main () {
  driver = wd('http://raspberrypi.local:7774/wd/hub');
  await driver.init({app});
  await B.delay(2000);
  try {
    const kick = await driver.elementById("A1");
    const snare = await driver.elementById("A2");
    const hat = await driver.elementById("A5");
    const tom = await driver.elementById("A6");
    const elMap = {k: kick, s: snare, h: hat, t: tom};
    const song = `
      k4 k4 s8 k4 k8
      k4 k4 s8 k8 s8 s8
      h4 k4 s8 k4 k8
      k4 k4 s8 k8 t8 t8
    `;
    await playSong(song, elMap);
  } finally {
    await driver.quit();
  }
})().catch(console.error);
