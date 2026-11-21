// Leonida Airlines Boarding Pass — GTA 6 meme on X (gta6-meme-x-01).
//
// The entry is the X post itself: this program only hands the house the
// post's address. It copies POST.json from this repository's root into the
// grader's output directory, byte for byte, and prints nothing on success.
//
// Node 22, standard library only. No network, no clock, no files outside
// this repository. Both runs of an entry must write the same bytes, so this
// program does a plain copy and nothing else.
//
// Paths are absolute, derived from this file's own location: the grader runs
// `node /bot/main.ts` from another working directory, so a relative path
// would point at the wrong place. MAKEFUN_OUTPUT_DIR is honoured when set
// (local runs), and defaults to /output (the grader).

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const REPO_ROOT = dirname(fileURLToPath(import.meta.url));
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const SOURCE = join(REPO_ROOT, 'POST.json');
const TARGET = join(OUTPUT_DIR, 'POST.json');

if (!existsSync(SOURCE)) {
  console.error(`POST.json not found in the repository root: ${SOURCE}`);
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(SOURCE, TARGET);
} catch (err) {
  console.error(`POST.json could not be copied to ${TARGET}: ${String(err)}`);
  process.exit(1);
}
