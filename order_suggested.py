class SuggestedOrder(object):
    """
    A SuggestedOrder object is generated by the PortfolioHandler
    to be sent to the PositionSizer object and subsequently the
    RiskManager object. Creating a separate object type for
    suggested orders and final orders (OrderEvent objects) ensures
    that a suggested order is never transacted unless it has been
    scrutinised by the position sizing and risk management layers.
    """
    def __init__(self, ticker, action, quantity=0):
        """
        Initialises the SuggestedOrder. The quantity defaults
        to zero as the PortfolioHandler creates these objects
        prior to any position sizing.
        The PositionSizer object will "fill in" the correct
        value prior to sending the SuggestedOrder to the
        RiskManager.
        Parameters:
        ticker - The ticker symbol, e.g. 'GOOG'.
        action - 'BOT' (for long) or 'SLD' (for short)
            or 'EXIT' (for liquidation).
        quantity - The quantity of shares to transact.
        """
        self.ticker = ticker
        self.action = action
        self.quantity = quantity