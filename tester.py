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

      # 2. Python 환경 설정
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      # 3. 종속성 캐싱 (pip 설치 속도 최적화)
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      # 4. 종속성 설치
      - name: Install dependencies
        run: pip install --no-cache-dir -r requirements.txt

      # 5. Python 최적화 설정
      - name: Optimize Python Execution
        run: |
          export PYTHONUNBUFFERED=1
          export PYTHONOPTIMIZE=2

      # 6. 테스트 실행
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

      # 7. 결과 보고
      - name: Autograding Reporter
        uses: classroom-resources/autograding-grading-reporter@v1
        env:
          TEST_RESULTS: "${{ steps.test.outputs.result }}"
        with:
          runners: "github-classroom"
