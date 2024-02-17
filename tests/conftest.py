import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def open_page(request, driver):
    page_class = request.param['class']
    page_url = request.param['url']

    class_object = page_class(driver, page_url)
    class_object.open_url()
    return class_object
