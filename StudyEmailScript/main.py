import ezgmail

BODY_TEXT = f"""<p>Hi there! This is a test.</p>"""

def main():
    adress = input("Input subject's address > ")
    if "@" not in adress:
        print("Ha ha, very funny.")
        quit()
    else:
        print("\n[.] Sending email...")
        ezgmail.send(adress, "Randomness", BODY_TEXT, ["20200618151441589.pdf"])
        print("[!] Email sent.")

if __name__ == '__main__':
    main()
