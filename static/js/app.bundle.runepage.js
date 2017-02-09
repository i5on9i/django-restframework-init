(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define([], factory);
	else {
		var a = factory();
		for(var i in a) (typeof exports === 'object' ? exports : root)[i] = a[i];
	}
})(this, function() {
return webpackJsonp([0],{

/***/ 184:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(86);


/***/ }),

/***/ 86:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
throw new Error("Cannot find module \"./runpage.css\"");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react__ = __webpack_require__(57);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_dom__ = __webpack_require__(56);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_utils_utils_js__ = __webpack_require__(87);
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }








var RunePage = function (_React$Component) {
    _inherits(RunePage, _React$Component);

    function RunePage() {
        _classCallCheck(this, RunePage);

        return _possibleConstructorReturn(this, _React$Component.apply(this, arguments));
    }

    RunePage.prototype.render = function render() {
        return __WEBPACK_IMPORTED_MODULE_1_react___default.a.createElement('div', { className: __WEBPACK_IMPORTED_MODULE_0__runpage_css___default.a.runepage });
    };

    RunePage.prototype.componentDidMount = function componentDidMount() {
        url = '/riotapi/';
        var _options = options,
            type = _options.type,
            url = _options.url,
            success = _options.success,
            error = _options.error,
            dataType = _options.dataType;

        return this.ajaxSend({
            url: url,
            type: 'GET',
            dataType: 'json',
            success: function success(res) {
                console.log(res);
            }

        });
    };

    return RunePage;
}(__WEBPACK_IMPORTED_MODULE_1_react___default.a.Component);

/* harmony default export */ __webpack_exports__["default"] = RunePage;

/***/ }),

/***/ 87:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* unused harmony export ajaxSend */


var ajaxSend = function ajaxSend(options) {
    var type = options.type,
        url = options.url,
        success = options.success,
        error = options.error,
        dataType = options.dataType;


    var xhr = new XMLHttpRequest();

    var _type = type || 'GET';
    xhr.open(type, encodeURI(url));
    xhr.responseType = dataType || '';

    // User-Agent
    // the below does not work, see background.js to change user-agent
    // xhr.setRequestHeader("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36")

    xhr.onload = function () {
        if (xhr.status === 200) {
            if (success !== 'undefined') {
                success(xhr.responseText);
            }
        } else {
            if (error !== 'undefined') {
                error(xhr, xhr.status);
            }
        }
    };
    xhr.send();
};

/***/ })

},[184]);
});