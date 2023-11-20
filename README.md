
<div>
    <div>  
        <h1>Prepare project</h1>
    </div>
    <div>
        <ul>
            <li><b>python -m venv venv</b></li>
            <li><b>source venv/bin/activate</b>(Linux, MacOS), <b>.\venv\Scripts\activate</b>(Windows CMD)</li>
            <li><b>pip install -r requirements.txt</b></li>
            <li><b>cd app</b></li>
            <li><b>uvicorn main:w_app</b></li>
        </ul>
    </div>
</div>


<div>
    <p>Для создание формы необходимо перейти на по адресу <b>/form/create</b> (на главной странице есть кнопка для перехода на эту страницу :D )</p>
    <p>Для поиска имени формы по заданному паттерну необходимо отправить post-запрос по адресу <b>/get_form</b></p>
</div>
<div>
    <p>В папке <b>app</b> существует готовая база данных - <b>database.json</b></p>
</div>

<div>
    <p> Для тестирования post-запроса в корневой папке есть файл request_test.py </p>
</div>
