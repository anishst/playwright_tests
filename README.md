# [Playwright](https://playwright.dev/docs/intro) Tests

- [run from command line](https://playwright.dev/python/docs/running-tests): ```pytest .\test_simple.py```
- [run with docker](https://playwright.dev/docs/docker)
  - build image: ```docker build -t playwrightimg .```
  - run container and remove it when done running tests: ```docker run -it --rm playwrightimg```