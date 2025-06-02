import unittest
from utils.GuessX1Time import guess_x1_time
from data.Data import data


class GuessX1TimeTest (unittest.TestCase):
    
    def test_guess_x1_time_matches (self):
        for d in data:
            self.assertEqual(guess_x1_time(d['script']), d['GuessX1TimeTest'])
            
            
    def test_guess_x1_time_no_matches (self):
        self.assertEqual(guess_x1_time('''<script type="text/javascript"> 
                (function(w, d, t, r, u) {
                var f, n, i;
                w[u] = w[u] || [], f = function() {
                    var o = {
                    ti: "5295101"
                    };
                    o.q = w[u], w[u] = new UET(o), w[u].push("pageLoad")
                }, n = d.createElement(t), n.src = r, n.async = 1, n.onload = n.onreadystatechange = function() {
                    var s = this.readyState;
                    s && s !== "loaded" && s !== "complete" || (f(), n.onload = n.onreadystatechange = null)
                }, i = d.getElementsByTagName(t)[0], i.parentNode.insertBefore(n, i)
                })(window, document, "script", "//bat.bing.com/bat.js", "uetq");
                </script>'''), '')