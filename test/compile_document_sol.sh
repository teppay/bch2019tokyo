#!/usr/bin/env bash
solc --bin ../contracts/document.sol | sed -e '1,3d' > document.bin