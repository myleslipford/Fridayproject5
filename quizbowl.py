import sqlite3
import random

def get_question_answer_from_database(cursor, table_name):
    cursor.execute(f"SELECT question, answer FROM {table_name};")
    return cursor.fetchall()

def play_quiz_bowl(quiz_data):
   
    # Play the Quiz Bowl game
    for question, answer in quiz_data:
        print("Question:", question)

        # Get user input for the answer
        user_answer = input("Your answer: ")

        # Check the answer
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {answer}\n")

def main():
    # Connect to the database
    conn = sqlite3.connect("FridayProj5.db")
    cursor = conn.cursor()

    # Get the list of tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Assuming there is only one table in your case
    if tables:
        table_name = tables[0][0]

        # Extract questions and answers from the specified table
        quiz_data = get_question_answer_from_database(cursor, table_name)

        # Play the Quiz Bowl game
        play_quiz_bowl(quiz_data)
    else:
        print("No tables found in the database.")

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
