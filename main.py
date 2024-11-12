from api.unit_of_work import UnitOfWork
from utils.user_input import get_user_command
from utils.display import display_posts
from utils.history_logger import log_user_request
from save_data import save_to_json, save_to_csv

def main():
    uow = UnitOfWork()
    command = get_user_command()

    if command == "show posts":
        posts = uow.fetch_and_commit()
        display_posts(posts)
        log_user_request(command, posts)
        save_to_json(posts)
        save_to_csv(posts)
    else:
        print("Невідома команда")

if __name__ == "__main__":
    main()