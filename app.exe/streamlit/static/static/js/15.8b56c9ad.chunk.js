(this["webpackJsonpstreamlit-browser"]=this["webpackJsonpstreamlit-browser"]||[]).push([[15],{1592:function(t,e){},1605:function(t,e){},1611:function(t,e){},1614:function(t,e){},1615:function(t,e){},1776:function(t,e,n){"use strict";n.r(e),n.d(e,"default",(function(){return Y}));var a=n(26),i=n(2),r=n(4),o=n(6),c=n(7),s=n(5),h=n(0),l=n(1767),u=n(1585),p=n.n(u),b=n(1690),j=n(76),d=n(27),m=n(1251),f=n(1774),O=n(1687),w=n(1689),g=n(1395),v=n(1784),x=n(1768),k=n(1604),S=n(215),y=n(10),T=n.n(y),V=n(70),C=n(146),L=n(66),M=n(463),E=n(220),F=n.n(E),N=n(99),P=n(42),z=function(t){Object(o.a)(n,t);var e=Object(c.a)(n);function n(){return Object(i.a)(this,n),e.apply(this,arguments)}return n}(Object(M.a)(Error)),D=function(t){Object(o.a)(n,t);var e=Object(c.a)(n);function n(){return Object(i.a)(this,n),e.apply(this,arguments)}return n}(Object(M.a)(Error)),J=function(){function t(){Object(i.a)(this,t)}return Object(r.a)(t,null,[{key:"get",value:function(){var e=Object(V.a)(T.a.mark((function e(){var n,a,i;return T.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(n=P.a.current,a=n.commandLine,i=n.userMapboxToken,t.token&&t.commandLine===a.toLowerCase()){e.next=10;break}if(""===i){e.next=6;break}t.token=i,e.next=9;break;case 6:return e.next=8,this.fetchToken("https://data.streamlit.io/tokens.json","mapbox");case 8:t.token=e.sent;case 9:t.commandLine=a.toLowerCase();case 10:return e.abrupt("return",t.token);case 11:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"fetchToken",value:function(){var t=Object(V.a)(T.a.mark((function t(e,n){var a,i,r;return T.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,F.a.get(e);case 3:if(a=t.sent,null!=(i=a.data[n])&&""!==i){t.next=7;break}throw new Error('Missing token "'.concat(n,'"'));case 7:return t.abrupt("return",i);case 10:throw t.prev=10,t.t0=t.catch(0),r=Object(N.a)(t.t0),new D("".concat(r.message," (").concat(e,")"));case 14:case"end":return t.stop()}}),t,null,[[0,10]])})));return function(e,n){return t.apply(this,arguments)}}()}]),t}();J.token=void 0,J.commandLine=void 0,J.isRunningLocal=function(){var t=window.location.hostname;return"localhost"===t||"127.0.0.1"===t};var B=n(108),I=n.n(B),q=n(147),A=n(1),G=function(t){var e=t.error,n=t.width,a=t.deltaType;return e instanceof z?Object(A.jsx)(q.a,{width:n,name:"No Mapbox token provided",message:Object(A.jsxs)(A.Fragment,{children:[Object(A.jsxs)("p",{children:["To use ",Object(A.jsxs)("code",{children:["st.",a]})," or ",Object(A.jsx)("code",{children:"st.map"})," you need to set up a Mapbox access token."]}),Object(A.jsxs)("p",{children:["To get a token, create an account at"," ",Object(A.jsx)("a",{href:"https://mapbox.com",children:"https://mapbox.com"}),". It's free for moderate usage levels!"]}),Object(A.jsxs)("p",{children:["Once you have a token, just set it using the Streamlit config option ",Object(A.jsx)("code",{children:"mapbox.token"})," and don't forget to restart your Streamlit server at this point if it's still running, then reload this tab."]}),Object(A.jsxs)("p",{children:["See"," ",Object(A.jsx)("a",{href:"https://docs.streamlit.io/library/advanced-features/configuration#view-all-configuration-options",children:"our documentation"})," ","for more info on how to set config options."]})]})}):e instanceof D?Object(A.jsx)(q.a,{width:n,name:"Error fetching Streamlit Mapbox token",message:Object(A.jsxs)(A.Fragment,{children:[Object(A.jsx)("p",{children:"This app requires an internet connection."}),Object(A.jsx)("p",{children:"Please check your connection and try again."}),Object(A.jsxs)("p",{children:["If you think this is a bug, please file bug report"," ",Object(A.jsx)("a",{href:"https://github.com/streamlit/streamlit/issues/new/choose",children:"here"}),"."]})]})}):Object(A.jsx)(q.a,{width:n,name:"Error fetching Streamlit Mapbox token",message:e.message})},R=function(t){return function(e){var n=function(n){Object(o.a)(h,n);var a=Object(c.a)(h);function h(t){var e;return Object(i.a)(this,h),(e=a.call(this,t)).initMapboxToken=Object(V.a)(T.a.mark((function t(){var n,a;return T.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,J.get();case 3:n=t.sent,e.setState({mapboxToken:n,isFetching:!1}),t.next=11;break;case 7:t.prev=7,t.t0=t.catch(0),a=Object(N.a)(t.t0),e.setState({mapboxTokenError:a,isFetching:!1});case 11:case"end":return t.stop()}}),t,null,[[0,7]])}))),e.state={isFetching:!0,mapboxToken:void 0,mapboxTokenError:void 0},e.initMapboxToken(),e}return Object(r.a)(h,[{key:"render",value:function(){var n=this.state,a=n.mapboxToken,i=n.mapboxTokenError,r=n.isFetching,o=this.props.width;return i?Object(A.jsx)(G,{width:o,error:i,deltaType:t}):r?Object(A.jsx)(C.a,{body:"Loading...",kind:L.a.INFO,width:o}):Object(A.jsx)(e,Object(s.a)({mapboxToken:a},this.props))}}]),h}(h.PureComponent);return n.displayName="withMapboxToken(".concat(e.displayName||e.name,")"),I()(n,e)}},W=n(43),_=n(9),H=Object(_.a)("div",{target:"e1q4dr931"})((function(t){var e=t.width,n=t.height;return{marginTop:t.theme.spacing.sm,position:"relative",height:n,width:e}}),""),K=Object(_.a)("div",{target:"e1q4dr930"})((function(t){var e=t.theme;return{position:"absolute",right:"2.625rem",top:e.spacing.md,zIndex:1,"button:not(:disabled)":{background:e.colors.bgColor,"& + button":{borderTopColor:e.colors.secondaryBg},"& span":{filter:Object(d.hasLightBackgroundColor)(e)?"":"invert(100%)"}}}}),""),Q=(n(1591),{classes:Object(s.a)(Object(s.a)(Object(s.a)(Object(s.a)({},m),w),O),g)});Object(k.b)([v.a,x.a]);var U=new f.a({configuration:Q}),X=function(t){Object(o.a)(n,t);var e=Object(c.a)(n);function n(){var t;Object(i.a)(this,n);for(var a=arguments.length,r=new Array(a),o=0;o<a;o++)r[o]=arguments[o];return(t=e.call.apply(e,[this].concat(r))).state={viewState:{bearing:0,pitch:0,zoom:11},initialized:!1,initialViewState:{}},t.componentDidMount=function(){t.setState({initialized:!0})},t.createTooltip=function(e){var n=t.props.element;if(!e||!e.object||!n.tooltip)return!1;var a=JSON.parse(n.tooltip);return a.html?a.html=t.interpolate(e,a.html):a.text=t.interpolate(e,a.text),a},t.interpolate=function(t,e){var n=e.match(/{(.*?)}/g);return n&&n.forEach((function(n){var a=n.substring(1,n.length-1);t.object.hasOwnProperty(a)&&(e=e.replace(n,t.object[a]))})),e},t.onViewStateChange=function(e){var n=e.viewState;t.setState({viewState:n})},t}return Object(r.a)(n,[{key:"render",value:function(){var t=n.getDeckObject(this.props),e=this.state.viewState;return Object(A.jsx)(H,{className:"stDeckGlJsonChart",width:t.initialViewState.width,height:t.initialViewState.height,children:Object(A.jsxs)(l.a,{viewState:e,onViewStateChange:this.onViewStateChange,height:t.initialViewState.height,width:t.initialViewState.width,layers:this.state.initialized?t.layers:[],getTooltip:this.createTooltip,ContextProvider:b.a.Provider,controller:!0,children:[Object(A.jsx)(b.c,{height:t.initialViewState.height,width:t.initialViewState.width,mapStyle:t.mapStyle&&("string"===typeof t.mapStyle?t.mapStyle:t.mapStyle[0]),mapboxApiAccessToken:this.props.mapboxToken}),Object(A.jsx)(K,{children:Object(A.jsx)(b.b,{className:"zoomButton",showCompass:!1})})]})})}}],[{key:"getDerivedStateFromProps",value:function(t,e){var i=n.getDeckObject(t);if(!p()(i.initialViewState,e.initialViewState)){var r=Object.keys(i.initialViewState).reduce((function(t,n){return i.initialViewState[n]===e.initialViewState[n]?t:Object(s.a)(Object(s.a)({},t),{},Object(a.a)({},n,i.initialViewState[n]))}),{});return{viewState:Object(s.a)(Object(s.a)({},e.viewState),r),initialViewState:i.initialViewState}}return null}}]),n}(h.PureComponent);X.getDeckObject=function(t){var e=t.element,n=t.width,a=t.height,i=t.theme,r=JSON.parse(e.json);if(!Object(W.n)(r.mapStyle)){var o=Object(d.hasLightBackgroundColor)(i)?"light":"dark";r.mapStyle="mapbox://styles/mapbox/".concat(o,"-v9")}return a?(r.initialViewState.height=a,r.initialViewState.width=n):(r.initialViewState.height||(r.initialViewState.height=500),e.useContainerWidth&&(r.initialViewState.width=n)),delete r.views,U.convert(r)};var Y=Object(j.f)(R("st.pydeck_chart")(Object(S.a)(X)))}}]);