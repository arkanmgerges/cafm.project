#!/bin/bash

BLUE="\x1b[34;21m"
GREEN="\x1b[32;21m"
YELLOW="\x1b[33;21m"
RED="\x1b[31;21m"
RESET="\x1b[0m"

CURRENT_DIR_PATH=$(dirname "$0")
CURRENT_DIR_NAME=$(dirname "$0" | xargs basename)
echo -e "${GREEN}Generating proto code in path ${BLUE}'${CURRENT_DIR_PATH}'${RESET}"
echo -e "${GREEN}Current dir name is ${BLUE}'${CURRENT_DIR_NAME}'${RESET}"
echo -e "${GREEN}Current dir path is ${BLUE}'${CURRENT_DIR_PATH}'${RESET}"

#rm -rf _generated/*
#TMPDIR="${CURRENT_DIR_PATH}"/tmpdir
#mkdir -p "$TMPDIR"
#SOURCE="${CURRENT_DIR_PATH}"
#rsync -av --exclude="$TMPDIR" --exclude="_generated" --exclude="generate.sh" "$SOURCE/" "$TMPDIR"
#echo -e ${YELLOW}
#python -m grpc_tools.protoc --python_out=_generated --grpc_python_out=_generated -I "$TMPDIR" "$TMPDIR"/*.proto "$TMPDIR"/**/*.proto
#echo -e ${RESET}
#wait
#cp identity/__init__.py _generated/identity
#cp project/__init__.py _generated/project
#
#rm -rf "$TMPDIR"


rm -fr _generated/*
#cp _gen__init__.py _generated/__init__.py
TMPDIR="${CURRENT_DIR_PATH}"/tmpdir
mkdir -p "$TMPDIR"
SOURCE="${CURRENT_DIR_PATH}"
#cp -R "$SOURCE"/*.proto "$TMPDIR"
#find ./ -name "*.proto" -not \( -path "$TMPDIR" -prune \)  -not \( -path _generated -prune \) -exec cp --parents '{}' "$TMPDIR" ';'
rsync -av --exclude="$TMPDIR" --exclude="_generated" --exclude="generate.sh" "$SOURCE/" "$TMPDIR"

echo -e ${YELLOW}
python -m grpc_tools.protoc --python_out=_generated --grpc_python_out=_generated -I "$TMPDIR" "$TMPDIR"/*.proto "$TMPDIR"/**/*.proto "$TMPDIR"/project/lookup/*.proto "$TMPDIR"/project/lookup/**/*.proto
echo -e ${RESET}
wait

rm -rf "$TMPDIR"
