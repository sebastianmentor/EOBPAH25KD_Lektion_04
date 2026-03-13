def kontext(to_be_handle):
    try:
        to_be_handle.__enter__()

    except:
        ...

    finally:
        to_be_handle.__exit__()