from django.utils.translation import gettext_lazy as _

FIRST = "First"
SECOND = "Second"
THIRD = "Third"
TERM = (
    (FIRST, "First"),
    (SECOND, "Second"),
    (THIRD, "Third"),
)


CASH = "Cash"
CHEAQUE = "Cheaque"
MPESA = "Mpesa"

PAYMENT_METHOD = ((CASH, "Cash"), (CHEAQUE, "Cheaque"), (MPESA, "Mpesa"))

PAID = "Paid"
NOT_PAID = "Not Paid"
PARTIALLY_PAID = "Partially Paid"
PAID_EXCESS = "Paid Excess"

PAYMENT_STATUS = (
    (PAID, "Fully Paid"),
    (NOT_PAID, "Not Paid"),
    (PARTIALLY_PAID, "Partially Paid"),
    (PAID_EXCESS, "Paid Excess"),
)

MALE = "Male"
FMALE = "Female"

GENDER = ((MALE, "Male"), (FMALE, "Female"))


A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"

GRADE = (
    (A, "A"),
    (B, "B"),
    (C, "C"),
    (D, "D"),
    (E, "E"),
    (F, "F"),
)


DRAFT = "D"
DELIVERED = "S"
PENDING = "P"

STATUS = (
    (DRAFT, _("Draft")),
    (DELIVERED, _("Delivered")),
    (PENDING, _("Pending")),
)
