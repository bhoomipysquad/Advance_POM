from pages.social_media_page import Social_Media


def test_social_media(setup):
    driver = setup
    sm = Social_Media(driver)
    sm.open_social_media_pages()
