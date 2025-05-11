import requests

def main():
    name = "Aditya Tiwari"
    reg_no = "0827AL221008"
    email = "adityatiwari220708@acropolis.in"

    gen_response = requests.post(
        "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
        json={
            "name": name,
            "regNo": reg_no,
            "email": email
        }
    )

    if gen_response.status_code != 200:
        print("Failed to generate webhook:", gen_response.text)
        return

    response_data = gen_response.json()
    access_token = response_data.get("accessToken")
    webhook_url = response_data.get("webhook")

    if not access_token or not webhook_url:
        print("Missing access token or webhook URL")
        return

    print("Webhook and AccessToken received successfully.")
    print("Access Token:", access_token)
    print("Webhook URL:", webhook_url)

    last_digit = int(reg_no[-1])
    if last_digit % 2 == 0:
        question = "Question 2"
        question_link = "https://drive.google.com/file/d/1pO1ZvmDqAZJv7TXRYsVben11Wp2HVb/view?usp=sharing"
    else:
        question = "Question 1"
        question_link = "https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing"

    print(f"\nYou are assigned: {question}")

    final_sql_query = """SELECT
    E1.EMP_ID,
    E1.FIRST_NAME,
    E1.LAST_NAME,
    D.DEPARTMENT_NAME,
    COUNT(E2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM
    EMPLOYEE E1
JOIN
    DEPARTMENT D ON E1.DEPARTMENT = D.DEPARTMENT_ID
LEFT JOIN
    EMPLOYEE E2 ON E1.DEPARTMENT = E2.DEPARTMENT
    AND E2.DOB > E1.DOB
GROUP BY
    E1.EMP_ID, E1.FIRST_NAME, E1.LAST_NAME, D.DEPARTMENT_NAME
ORDER BY
    E1.EMP_ID DESC;"""

    if "your_table" in final_sql_query:
        print("\nPlease update 'final_sql_query' with the actual solution before submitting.")
        return

    print("\nSubmitting your final SQL query...")
    test_response = requests.post(
        "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON",
        headers={
            "Authorization": access_token,
            "Content-Type": "application/json"
        },
        json={
            "finalQuery": final_sql_query
        }
    )

    if test_response.status_code == 200:
        print("Submission successful!")
        print("Response:", test_response.json())
    else:
        print("Submission failed:")
        print(test_response.status_code, test_response.text)

if _name_ == "_main_":
    main()
