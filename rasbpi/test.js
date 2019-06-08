const wd = require('wd').promiseChainRemote;

(async function main () {
  driver = wd('http://raspberrypi.local:7774/wd/hub');
  await driver.init({});
  try {
  } finally {
    await driver.quit();
  }
})().catch(console.error);
