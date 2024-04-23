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

actions = {
    'Cash': [create_transaction, receive_cash, print_payment_receipt, return_payment_receipt, complete_transaction, close_transaction],
    'Credit': [create_transaction, request_account_credit_details, request_payment_from_bank, confirm_payment_approval_from_bank, close_transaction],
    'Fund Transfer': [create_transaction, fund_transfer, provide_bank_deposit_details, confirm_payment_approval_from_bank, close_transaction],
    'Cancel': [cancel_transaction, close_transaction]
}

payment_process = lambda payment_type: list(map(lambda action: action(), actions.get(payment_type, actions['Cancel'])))

print(payment_process('Cash'))
print(payment_process('Credit'))
print(payment_process('Fund Transfer'))
print(payment_process('Other')) 