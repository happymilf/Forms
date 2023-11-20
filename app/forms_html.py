


def phone_input(field_name_text : str = "Phone number", field_id : str = "input-phone") -> str:

    input_tel_html : str = f'<input type="tel" id="{field_id}" name="phone_number" placeholder="+7 (999) 999-99-99" maxlength="18" pattern="\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}">'
    
    result : str = f"<p>{field_name_text} {input_tel_html}</p>"
    
    return result
    

def date_input(field_name_text : str = "Date", field_id : str = "input-date", datetime : bool = False) -> str:
    date_type : str = "datetime-local" if datetime else "date"

    input_date_html : str = f'<input type="{date_type}" id="{field_id}" name="{date_type}" >'
    
    result : str = f'<p>{field_id}</p> {input_date_html}'


def text_input(field_name_text : str = "Text", field_id : str = "input-text") -> str:

    input_text_html : str = f'<input type="text" name="input" id="{field_id}">'

    result : str = f"<p>{field_name_text}</p>{input_text_html}"
    
    return result


def email_input(field_name_text : str = "Email", field_id : str = "input-email") -> str:

    input_email_html : str = f'<input type="email" name="email" id="{field_id}">'

    result : str = f'<p>{field_name_text}</p>{input_email_html}'

    return result