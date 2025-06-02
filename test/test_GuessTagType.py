import unittest
from utils.GuessTagType import guess_tag_type
from data.Data import data


class GuessTagTypeTest(unittest.TestCase):
    
    def test_guess_tag_type_matches (self):
        for d in data:
            self.assertEqual(guess_tag_type(d['script']), d['GuessTagTypeResult'])
            
    def test_guess_tag_type_no_matches (self):
        self.assertEqual(guess_tag_type('''<script type="text/javascript"> 
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
            })(window, document, "script", "//bat.bing.com/bat", "uetq");
            </script>'''), '')