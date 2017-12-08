$(document).ready(function() {
    $.ajax({
        url: "http://0.0.0.0:8080/get_crypto",
        success: function(response) {
            var crypt_list =
                 ['ADA', 'ADT', 'ARK', 'BCH', 'BCN', 'BTC', 'DASH', 'ETC',
                  'ETH', 'GAS', 'HSR', 'LSK', 'LTC', 'NEO', 'OMG', 'PAY',
                  'QTUM', 'SC', 'STEEM', 'STRAT', 'WAVES', 'XEM', 'XLM', 'XMR',
                  'XRP', 'ZEC', 'ZEN'];

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
