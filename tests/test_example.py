

def test_first(driver):
    driver.get("http://192.168.0.216:8081")
    assert "Your Store" == driver.title

