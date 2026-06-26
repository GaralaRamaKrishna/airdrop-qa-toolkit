from datetime import datetime


def take_screenshot(driver, test_name):
    """
    Take a screenshot of the browser and save it to the screenshots/ folder.

    This runs automatically when a check fails, so you can see exactly
    what the page looked like at the moment something went wrong.

    The filename includes the test name and the exact time it was taken.
    Example: Bitget Wallet_20240101_120000.png
    """

    # Create a filename using the campaign name and current time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{test_name}_{timestamp}.png"

    # Save the screenshot to that file
    driver.save_screenshot(filename)

    return filename