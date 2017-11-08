$(document).ready(function() {
    $.ajax({
        url: "http://0.0.0.0:8080/get_crypto",
        success: function(response) {
            var crypt_list =
                 ['ADT', 'ARK', 'BTC', 'BCH', 'BCN', 'ADA', 'DASH', 'ETH',
                  'ETC', 'GAS', 'HSR', 'LSK', 'LTC', 'XMR', 'NEM', 'NEO', 'OMG',
                  'QTUM', 'XRP', 'SC', 'STEEM', 'XLM', 'STRAT', 'PAY', 'WAVES',
                  'ZEC', 'ZEN']

            var parsed = JSON.parse(response.items);

            for (var i = 0; i < parsed.length; i++) {
                var id_tag = "#" + crypt_list[i];
                $(id_tag).html(parsed[i].price);
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
});
