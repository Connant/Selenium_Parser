# Selenium Parser

This project is a web scraping tool that uses Selenium to take screenshots of web pages. It navigates through a list of URLs, maximizes the browser window to the size of the entire page, and saves a screenshot in a structured directory path based on the URL.

## Requirements

- Python 3.9
- `selenium` package

## Configuration

1. **Setup Virtual Environment:**
   
   Create a virtual environment to manage dependencies.

   ```bash
   python3.9 -m venv venv
   ```

2. **Activate the Virtual Environment:**

   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```

   On Unix or MacOS:
   ```bash
   source venv/bin/activate
   ```

3. **Install Selenium:**

   ```bash
   pip install selenium
   ```

4. **Download ChromeDriver:**

   Make sure you have ChromeDriver downloaded and placed in your system PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

5. **Update `links.py`:**

   Add the URLs you want to scrape in `links.py`:

   ```python
   all_links = [
       "https://example.com",
       "https://example.com/other-path",
   ]
   ```

## Usage

To run the script, simply execute `main.py`:

```bash
python main.py
```

The script will iterate through the list of URLs, attempt to access each one, and capture a screenshot if successful. Screenshots will be saved in structured directories based on the URL paths.

## Example Output

Upon running the script, you will see console output indicating the status of each URL:

```
[1] OK!
 Parsing URL: https://example.com
 Screenshot_path: general/cq_example_com.png

[2] OK!
 Parsing URL: https://example.com/other-path
 Screenshot_path: other-path/cq_other_path.png
```

## Notes

- Ensure that your internet connection is stable.
- The script defaults to a 60-second timeout for loading pages and implicitly waits for elements up to 60 seconds.
- If the script encounters an error, it will retry up to 3 times before skipping the URL.

---
