#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
out="${root%/*}/NOVA_Web_Search_Agent_v4_Complete.zip"
rm -f "$out"
cd "$(dirname "$root")"
zip -qr "$out" "$(basename "$root")" -x '*/.pytest_cache/*' '*/__pycache__/*' '*.pyc'
echo "$out"
