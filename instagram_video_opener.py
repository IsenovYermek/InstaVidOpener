import requests
from bs4 import BeautifulSoup
import webbrowser


def open_instagram_video(url):
    try:
        response = requests.get(url, timeout=50)
        response.raise_for_status() # Проверка кода состояния ответа
        soup = BeautifulSoup(response.text, "html.parser")
        video_url_tag = soup.find("meta", property="og:video")
        if video_url_tag:
            video_url = video_url_tag["content"]
            webbrowser.open(video_url)
        else:
            print("URL видео не найден на странице Instagram")
    except requests.exceptions.RequestException as e:
        print("Ошибка при выполнении запроса:", e)
    except requests.exceptions.HTTPError as e:
        print("Ошибка кода состояния ответа:", e)
    except (KeyError, TypeError):
        print("URL видео не найден или недействителен")