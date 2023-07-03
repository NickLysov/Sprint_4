from selenium.webdriver.common.by import By


class OrderPageLocators:
    LOCATOR_NAME_FIELD_ORDER = (By.XPATH, "//input[@placeholder='* Имя']")                                              # Поле ввода имени на странице заказа
    LOCATOR_SURNAME_FIELD_ORDER = (By.XPATH, "//input[@placeholder='* Фамилия']")                                       # Поле ввода фамилии на странице заказа
    LOCATOR_ADDRESS_FIELD_ORDER = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")                    # Поле ввода адреса на странице заказа
    LOCATOR_METRO_FIELD_ORDER = (By.XPATH, "//input[@placeholder='* Станция метро']")                                   # Поле ввода станции метро на странице заказа
    LOCATOR_TNUMBER_FIELD_ORDER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")              # Поле ввода телефона на странице заказа
    LOCATOR_DATA_FIELD_ORDER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")                           # Поле ввода даты на странице заказа
    LOCATOR_ARENDA_FIELD_ORDER = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")                                  # Поле выбора срока аренды на странице заказа
    LOCATOR_CALENDAR_FIELD_ORDER = (By.XPATH, "//div[contains(text(),'12')]")                                           # Выбор даты в календаре
    LOCATOR_COMMENT_FIELD_ORDER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")                         # Поле ввода комментария для курьера на странице заказа
    LOCATOR_GREY_COLOR_ORDER = (By.XPATH, "//input[@id='grey']")                                                        # Чек-бокс выбора серого самоката
    LOCATOR_BLACK_COLOR_ORDER = (By.XPATH, "//input[@id='black']")                                                      # Чек-бокс выбора черного самоката
    LOCATOR_ZAKAZAT_ORDER = (By.XPATH, "//button[contains(text(),'Назад')]/following-sibling::*")                       # Кнопка перехода к подтверждению заказа
    LOCATOR_BACK_ORDER = (By.XPATH, "//button[contains(text(),'Назад')]")                                               # Кнопка возврата на первую панель оформления заказа
    LOCATOR_APPRUVE_ORDER = (By.XPATH, "//div[contains(text(),'Хотите оформить заказ?')]")                              # Панель подтверждения заказа
    LOCATOR_CANCEL_APPRUVE_ORDER = (By.XPATH, "//button[contains(text(),'Нет')]")                                       # Кнопка отмены подтверждения заказа
    LOCATOR_CONFIRM_APPRUVE_ORDER = (By.XPATH, "//button[contains(text(),'Да')]")                                       # Кнопка подтверждения заказа
    LOCATOR_FIELD_NUMBER_ORDER = (By.XPATH, "//div[contains(text(),'Номер')]")                                          # Поле с номером заказа
    LOCATOR_CHECK_BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")                           # Кнопка просмотра статуса заказа
    LOCATOR_SEARCH_SELECT = (By.XPATH, "//div[contains(text(),'Сокольники')]")                                          # Выбор метро Сокольники в выпадающем списке при заказе
    LOCATOR_NEXT_PANEL_ORDER = (By.XPATH, "//button[contains(text(),'Далее')]")                                         # Кнопка Далее в поле заказа
    LOCATOR_TERM_SELECT = (By.XPATH, "//div[contains(text(),'сутки')]")                                                 # Выбор срока аренды
    LOCATOR_YA_LINK = (By.XPATH, "//a[1]")                                                                              # Ссылка в хедере для перехода на Яндекс.ру
    LOCATOR_SAMOKAT_LINK = (By.XPATH, "//a[2]")
    LOCATOR_SAMOKAT_PAGE = (By.XPATH, "//a[2]")
    LOCATOR_NEW_PAGE = (By.TAG_NAME, "title")