#!/bin/bash

set -e

MAX_LOOPS=10
PROMPT_FILE="PROMPT.md"

echo "🚀 Ralph Wiggum 開始"

for i in $(seq 1 $MAX_LOOPS); do
  echo ""
  echo "========== ループ $i / $MAX_LOOPS =========="
  
  PROMPT=$(cat "$PROMPT_FILE")
  
  OUTPUT=$(gemini -y "$PROMPT" 2>&1)
  
  echo "$OUTPUT"
  
  if echo "$OUTPUT" | grep -q "<promise>COMPLETE</promise>"; then
    echo ""
    echo "✅ 全タスク完了！"
    exit 0
  fi
  
  echo "⏳ 次のループへ..."
  sleep 2
done

echo ""
echo "⚠️ 最大ループ回数に到達。手動確認してください。"
exit 1
