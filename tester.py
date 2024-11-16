name: Autograding Tests
'on':
  - push
  - repository_dispatch
permissions:
  checks: write
  actions: read
  contents: read
jobs:
  run-autograding-tests:
    runs-on: ubuntu-latest
    if: github.actor != 'github-classroom[bot]'
    steps:
      # 1. 레포지토리 코드 체크아웃
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. 테스트 실행
      - name: Run Test
        id: test
        uses: classroom-resources/autograding-io-grader@v1
        with:
          test-name: "circle-calculation"
          setup-command: ""
          command: python tester.py
          input: ""
          expected-output: |-
            c = 5.0
            area = 314.1592653589793
          comparison-method: contains
          timeout: 10

      # 3. 결과 보고
      - name: Autograding Reporter
        uses: classroom-resources/autograding-grading-reporter@v1
        env:
          TEST_RESULTS: "${{ steps.test.outputs.result }}"
        with:
          runners: "github-classroom"
