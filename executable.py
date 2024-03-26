try:
    import utils.main
    utils.main
except Exception as e:
    print(f'The error {str(e)} has happenned!')
    from config.firebase import Firebase
    fire = Firebase()
    fire.post_error('Python Default Script',str(e))