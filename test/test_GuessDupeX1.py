import unittest
from utils.GuessDupeX1 import guess_dupe_x1
from data.Data import data

class GuessDupeX1Test(unittest.TestCase):
    
    def test_guess_dupe_x1_matches(self):
        for d in data:
            self.assertEqual(guess_dupe_x1(d['script']), d['GuessDupeX1Result'])
            
        
    def test_guess_dupe_x1_no_script(self):
        self.assertEqual('', '')
    
            
    def test_guess_dupe_x1_no_matches(self):
        for d in data:
            self.assertEqual(guess_dupe_x1('''<script type="text/javascript"> 
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
                </script>'''), "")