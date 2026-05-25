#!/usr/bin/env node
// Usage: node scripts/screenshot-slide.js <url> <output-path> [--width 1280] [--height 720]
// Requires: npm install playwright + npx playwright install chromium
// The local server must already be running (python3 -m http.server 8080 --directory .)

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function main() {
  const args = process.argv.slice(2);
  if (args.length < 2) {
    console.error('Usage: node screenshot-slide.js <url> <output-path> [--width N] [--height N]');
    process.exit(1);
  }

  const url = args[0];
  const outputPath = args[1];

  let width = 1280;
  let height = 720;
  for (let i = 2; i < args.length; i++) {
    if (args[i] === '--width') width = parseInt(args[i + 1]);
    if (args[i] === '--height') height = parseInt(args[i + 1]);
  }

  const dir = path.dirname(outputPath);
  if (dir && !fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width, height });
  await page.goto(url, { waitUntil: 'networkidle' });

  // Wait for Reveal.js to initialise
  await page.waitForFunction(() => typeof Reveal !== 'undefined' && Reveal.isReady(), { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(500);

  await page.screenshot({ path: outputPath, fullPage: false });
  await browser.close();

  console.log(JSON.stringify({ url, output: outputPath, width, height, ts: new Date().toISOString() }));
}

main().catch(err => { console.error(err.message); process.exit(1); });
