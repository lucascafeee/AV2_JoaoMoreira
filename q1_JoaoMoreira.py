create_transaction = lambda: "Transaction created"
receive_cash = lambda: "Cash received"
print_payment_receipt = lambda: "Payment receipt printed"
return_payment_receipt = lambda: "Payment receipt returned"
complete_transaction = lambda: "Transaction completed"
fund_transfer = lambda: "Fund transferred"
provide_bank_deposit_details = lambda: "Bank deposit details provided"
request_account_credit_details = lambda: "Account credit details requested"
request_payment_from_bank = lambda: "Payment request sent to bank"
confirm_payment_approval_from_bank = lambda: "Payment approved by bank"
close_transaction = lambda: "Transaction closed"
cancel_transaction = lambda: "Transaction cancelled"

def payment_process_pyth(payment_type):
    get_actions = lambda payment_type: (
        [create_transaction, receive_cash, print_payment_receipt, return_payment_receipt, complete_transaction, close_transaction] if payment_type == "Cash" else
        [create_transaction, request_account_credit_details, request_payment_from_bank, confirm_payment_approval_from_bank, close_transaction] if payment_type == "Credit" else
        [create_transaction, fund_transfer, provide_bank_deposit_details, confirm_payment_approval_from_bank, close_transaction] if payment_type == "Fund Transfer" else
        [cancel_transaction, close_transaction]
    )
    
    execute_actions = lambda actions: [action() for action in actions]
    return execute_actions(get_actions(payment_type))

print(payment_process_pyth('Cash'))
print(payment_process_pyth('Credit'))
print(payment_process_pyth('Fund Transfer'))
print(payment_process_pyth('Other'))
