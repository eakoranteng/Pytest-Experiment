"""
Test module for Wallet
"""

import pytest
from wallet import Wallet, InsufficientAmount


def test_default_initial_amount():
    """
    Test case for verifying the default initial amount of a Wallet.

    It creates a Wallet instance and checks if the balance is 0.
    """
    wallet = Wallet()

    assert wallet.balance == 0


def test_setting_initial_amount():
    """
    Test case for verifying setting the initial amount of a Wallet.

    It creates a Wallet instance with an initial amount of 100 and checks if the balance is set correctly.
    """
    wallet = Wallet(100)

    assert wallet.balance == 100


def test_wallet_add_cash():
    """
    Test case for verifying adding cash to a Wallet.

    It creates a Wallet instance with an initial amount of 10, adds 90 to it, and checks if the balance is 100.
    """
    wallet = Wallet(10)

    wallet.add_cash(90)

    assert wallet.balance == 100


def test_wallet_spend_cash():
    """
    Test case for verifying spending cash from a Wallet.

    It creates a Wallet instance with an initial amount of 20, spends 10 from it, and checks if the balance is 10.
    """
    wallet = Wallet(20)

    wallet.spend_cash(10)

    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    """
    Test case for verifying that spending cash raises an InsufficientAmount exception on insufficient balance.

    It creates a Wallet instance and attempts to spend 100 from it, expecting an InsufficientAmount exception.
    """
    wallet = Wallet()

    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
