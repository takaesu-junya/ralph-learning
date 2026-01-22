# 指示

あなたはTo-Doリスト CLI を開発するエンジニアです。

## ルール

1. PRD.json を読み、`done: false` かつ最も若いIDのstoryを1つだけ選択せよ
2. そのstoryのみを実装せよ
3. `pytest` で全テストがpassすることを確認せよ
4. 作業内容を `progress.txt` に追記せよ（既存内容は消さない）
5. PRD.json の該当storyを `done: true` に更新せよ
6. git add && git commit せよ
7. 全storyが `done: true` なら、最後に `<promise>COMPLETE</promise>` と出力せよ

## 技術スタック

- Python 3.x
- pytest（テスト）
- JSON（データ保存）

## 重要

- 1つのstoryだけに集中すること
- 既存コードを壊さないこと
- テストがpassしない状態でcommitしないこと
- To-Doデータは `todos.json` に保存すること
- 完全なCRUD操作（Create, Read, Update, Delete）を実装すること
