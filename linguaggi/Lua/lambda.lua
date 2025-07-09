A = function(s) {
	B = function(z) { return s(z); }
	return B(s);
}