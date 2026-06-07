from restapi.constants.order_status import TestStatus


ALLOWED_TRANSITIONS = {
    TestStatus.PENDING: [
        TestStatus.COLLECTED,
        TestStatus.CANCELLED,
    ],

    TestStatus.COLLECTED: [
        TestStatus.SHIPPED,
        TestStatus.RESULT_PENDING,
        TestStatus.RESAMPLING,
        TestStatus.REJECTED,
        TestStatus.CANCELLED,
    ],

    TestStatus.SHIPPED: [
        TestStatus.RECEIVED,
        TestStatus.CANCELLED,
    ],

    TestStatus.RECEIVED: [
        TestStatus.RESULT_PENDING,
        TestStatus.RESAMPLING,
        TestStatus.REJECTED,
    ],

    TestStatus.RESAMPLING: [
        TestStatus.COLLECTED,
        TestStatus.CANCELLED,
    ],

    TestStatus.RESULT_PENDING: [
        TestStatus.RESULT_ENTERED,
    ],

    TestStatus.RESULT_ENTERED: [
        TestStatus.AUTHORIZED,
    ],

    TestStatus.AUTHORIZED: [
        TestStatus.COMPLETED,
    ],

    TestStatus.REJECTED: [],

    TestStatus.COMPLETED: [],

    TestStatus.CANCELLED: [],
}


class InvalidStatusTransitionError(Exception):
    pass


def transition_test_status(current_status, new_status):
    allowed = ALLOWED_TRANSITIONS.get(
        current_status,
        [],
    )

    if new_status not in allowed:
        raise InvalidStatusTransitionError(
            f"Cannot transition from "
            f"'{current_status}' "
            f"to "
            f"'{new_status}'. "
            f"Allowed transitions: "
            f"{[status.value for status in allowed]}"
        )

    return True