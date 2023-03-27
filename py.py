html.Div(
    [
        html.P("Filter by Resistance", className="control_label"),
        html.Div(
            # Resistance Picker
            dcc.Checklist(
                id="resistance_picker",
                className="dcc_control",
                value=[],
                options=[
                    {'label': 'Frizz', 'value': 'Frizz'},
                    {'label': 'Sizz', 'value': 'Sizz'},
                    {'label': 'Crack', 'value': 'Crack'},
                    {'label': 'Woosh', 'value': 'Woosh'},
                    {'label': 'Bang', 'value': 'Bang'},
                    {'label': 'Zap', 'value': 'Zap'},
                    {'label': 'Zam', 'value': 'Zam'},
                ],
                persistence_type='session',
                persistence=True,
                style={'max-height': '350px', 'overflow': 'auto'}
            ),
            className="row flex-display",
            ),
    ],
    className="pretty_container two columns",
),
html.Div(
    [
        html.P("Filter by Weakness", className="control_label"),
        html.Div(
            # Weakness PIcker
            dcc.Checklist(
                id="weakness_picker",
                className="dcc_control",
                value=[],
                options=[
                    {'label': 'Frizz', 'value': 'Frizz'},
                    {'label': 'Sizz', 'value': 'Sizz'},
                    {'label': 'Crack', 'value': 'Crack'},
                    {'label': 'Woosh', 'value': 'Woosh'},
                    {'label': 'Bang', 'value': 'Bang'},
                    {'label': 'Zap', 'value': 'Zap'},
                    {'label': 'Zam', 'value': 'Zam'},
                ],
                persistence_type='session',
                persistence=True,
                style={'max-height': '350px', 'overflow': 'auto'}
            ),
            className="row flex-display",
            ),
    ],
    className="pretty_container two columns",
),
