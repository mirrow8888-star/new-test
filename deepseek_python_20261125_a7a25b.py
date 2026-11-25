def mail_send(api_key, sender, to, subject, html, text, attachments):
    """透過 Resend Python SDK 寄信，回傳郵件 id。"""
    import resend
    
    resend.api_key = api_key
    
    # 處理附件（SDK 需要 base64 字串與檔名）
    resend_attachments = []
    if attachments:
        resend_attachments = [
            {"filename": n, "content": base64.b64encode(b).decode("ascii")} 
            for n, b in attachments
        ]

    params = {
        "from": sender,
        "to": to,
        "subject": subject,
        "html": html,
        "text": text,
    }
    if resend_attachments:
        params["attachments"] = resend_attachments

    try:
        email = resend.Emails.send(params)
        return email.get("id", "")
    except Exception as e:
        raise MailError(f"Resend SDK 錯誤：{str(e)}")