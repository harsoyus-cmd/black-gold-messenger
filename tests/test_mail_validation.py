from core.mail.mail import (
    create_mail_content,
    validate_body,
    validate_subject,
)


def expect_error(function):
    try:
        function()
    except (TypeError, ValueError):
        return True

    return False


assert expect_error(lambda: validate_subject(""))
assert expect_error(lambda: validate_subject("   "))
assert expect_error(lambda: validate_subject(123))

assert expect_error(lambda: validate_body(""))
assert expect_error(lambda: validate_body("   "))
assert expect_error(lambda: validate_body(123))

message = create_mail_content(
    "BGM Test",
    "Pesan Unicode 🌍",
)

assert message["subject"] == "BGM Test"
assert message["body"] == "Pesan Unicode 🌍"

print("BGM Mail validation: PASS")
