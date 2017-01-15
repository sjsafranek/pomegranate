
	var FeatureFormView = Backbone.View.extend({

	    el: "#featureSubmitModal",

	    initialize: function(marker, csrf_token){
	    	var self = this;
	        _.bindAll(
	        	this, 
	        	'render',
				'clearForm',
				'roomTemplate',
				'zoneTemplate',
				'personTemplate',
				'furnitureTemplate',
				'submitPerson',
				'submitFurniture',
				'ajaxPost',
				'ajaxResponseHandler',
				'submit'
	        );
	        this.marker = marker;
	        this.csrf_token = csrf_token;
			this.render();
	    },

	    events: {
	        "change #formFeatureType": "clearForm",
	        'click #submitFeature': "submit"
	    },

	    submit: function(e) {
	    	var self = this;
			swal({
				title: "Are you sure?",
				text: "Your will not be able to edit data!",
				type: "warning",
				showCancelButton: true,
				confirmButtonClass: "btn-danger",
				confirmButtonText: "Yes, submit data!",
				showLoaderOnConfirm: true,
				closeOnConfirm: false
			},
			function(){
				// Submitting feature
				var featureType = $("#formFeatureType").val();
		    	switch(featureType) {
				    case "Room":
				        // self.submitRoom();
				        // break;
				    case "Zone":
				        // self.submitZone();
				        // break;
				    case "Person":
				        self.submitPerson();
				        break;
				    default:
				        self.submitFurniture();
				}
			});
	    },

	    submitPerson: function(e) {
	    	var self = this;
			var elems = this.$el.find(".featureAttribute");
			payload = {};
			for (var i=0; i < elems.length; i++) {
				payload[$(elems[i]).attr("id")] = $(elems[i]).val();
			}
			payload.longitude = this.marker.getLatLng().lng;
			payload.latitude = this.marker.getLatLng().lat;
			payload.csrf_token = this.csrf_token;
			this.ajaxPost("/api/v1/person", payload, this.ajaxResponseHandler);
	    },

	    submitFurniture: function(e) {
	    	var self = this;
			var elems = this.$el.find(".featureAttribute");
			payload = {};
			for (var i=0; i < elems.length; i++) {
				payload[$(elems[i]).attr("id")] = $(elems[i]).val();
			}
			payload.longitude = this.marker.getLatLng().lng;
			payload.latitude = this.marker.getLatLng().lat;
			payload.csrf_token = this.csrf_token;
			this.ajaxPost("/api/v1/furniture", payload, this.ajaxResponseHandler);
	    },

	    ajaxPost: function(url, payload, callback) {
			$.ajax({
	            type: "POST",
	            data:  JSON.stringify(payload),
	            url: url,
	            dataType: 'JSON',
	            success: function (data) {
	                callback(null, data);
	            },
	            error: function(xhr,errmsg,err) {
	                callback(new Error(errmsg));
	            }
	        });
	    },

	    ajaxResponseHandler: function(error, result) {
	    	if (error) {
	    		swal("Error!", error, "error");
	    		return;
	    	}
	    	if ("ok" != result.status) {
	    		swal("Error!", JSON.stringify(result), "error");
	    	} else {
	    		swal("Submitted!", JSON.stringify(result), "success");
	    	}
	    	// setTimeout(function () {
	    	// 	swal("Submitted!", "Your data has been submitted.", "success");
	    	// 	self.$el.modal('hide');
	    	// }, 2000);
	    },

	    roomTemplate: function(e) {
            return '<div class="form-group">'
                + '    <label for="noise"> Messy</label>'
                + '    <select class="form-control featureAttribute" id="messy">'
                + '        <option value="false">False</option>'
                + '        <option value="true">True</option>'
                + '    </select>'
                + '</div>'
                + '<div class="form-group">'
                + '    <label for="noise"> Noise</label>'
                + '    <input type="number" min="1" max="5" value="1" class="form-control featureAttribute" id="noise">'
                + '</div>';
	    },
	    
	    zoneTemplate: function(e) {
            return '<div class="form-group">'
                + '    <label for="outlets_used"> Outlets inuse</label>'
                + '    <input type="number" min="0" value="0" class="form-control featureAttribute" id="outlets_used">'
                + '</div>';
	    },
	    
	    personTemplate: function(e) {
			return '<div class="form-group">'
                + '    <label for="person_type"> Person Type</label>'
                + '    <select class="form-control featureAttribute" id="person_type">'
                + '        <option value="ACADEMIC">Academic</option>'
                + '        <option value="PUBLIC">Public</option>'
                + '    </select>'
                + '</div>'
                + '<div class="form-group">'
                + '    <label for="computer_type"> Computer Type</label>'
                + '    <select class="form-control featureAttribute" id="computer_type">'
                + '        <option value="NONE">None</option>'
                + '        <option value="DESKTOP">Desktop</option>'
                + '        <option value="LAPTOP">Laptop</option>'
                + '    </select>'
                + '</div>'
                + '<div class="form-group">'
                + '    <label for="collab"> Collab</label>'
                + '    <select class="form-control featureAttribute" id="collab">'
                + '        <option value="false">False</option>'
                + '        <option value="true">True</option>'
                + '    </select>'
                + '</div>';
	    },


	    furnitureTemplate: function(e) {
			return '<div class="form-group">'
                + '    <label for="uuid"> UUID</label>'
                + '    <input type="text" class="form-control featureAttribute" disabled id="uuid">'
                + '</div>'
                + '<div class="form-group">'
                + '    <label for="rfid"> RFID</label>'
                + '    <input type="text" class="form-control featureAttribute" id="rfid">'
                + '</div>'

                + '<div class="form-group">'
                + '    <label for="furniture_type"> Furniture Type</label>'
                + '    <select class="form-control featureAttribute" id="furniture_type">'
                + '        <option value="COUCH">Couch</option>'
                + '        <option value="CHAIR ARM">Chair (ARM)</option>'
                + '        <option value="CHAIR TALL">Chair (TALL)</option>'
                + '        <option value="CHAIR YELLOW">Chair (YELLOW)</option>'
                + '        <option value="CHAIR GREY">Chair (GREY)</option>'
                + '        <option value="CHAIR ARMLESS">Chair (ARMLESS)</option>'
                + '        <option value="TABLE TALL">Table (TALL)</option>'
                + '        <option value="TABLE SHORT">Table (SHORT)</option>'
                + '        <option value="TABLE REGULAR">Table (REGULAR)</option>'
                + '        <option value="TABLE GLASS">Table (GLASS)</option>'
				+ '        <option value="DESK PUBLIC">Desk (PUBLIC)</option>'
				+ '        <option value="DESK CONSULTATION">Desk (CONSULTATION)</option>'
				+ '        <option value="DESK TALL">Desk (TALL)</option>'
				+ '        <option value="DESK OSX">Desk (OSX)</option>'
				+ '        <option value="DESK WIN">Desk (WIN)</option>'
				+ '        <option value="DESK OSX w/ SCANNER">Desk (OSX w/ SCANNER)</option>'
				+ '        <option value="DESK WIN w/ SCANNER">Desk (WIN w/ SCANNER)</option>'
				+ '        <option value="DESK LAPTOP">Desk (LAPTOP)</option>'
				+ '        <option value="TABLE BIG MAP">Table (BIG MAP)</option>'
                + '    </select>'
                + '</div>';
	    },


	    clearForm: function(e) {
	    	this.$el.find("#featureSubmitForm .form-group").remove();

	    	var featureType = $("#formFeatureType").val();
	    	switch(featureType) {
			    case "Room":
			        this.$el.find("#featureSubmitForm").prepend(
			        	this.roomTemplate()
			        );
			        break;
			    case "Zone":
			        this.$el.find("#featureSubmitForm").prepend(
			        	this.zoneTemplate()
			        );
			        break;
			    case "Person":
			        this.$el.find("#featureSubmitForm").prepend(
			        	this.personTemplate()
			        );
			        break;
			    default:
			        this.$el.find("#featureSubmitForm").prepend(
			        	this.furnitureTemplate()
			        );
			}
	    },

	    render: function(e) {
	    	var self = this;
	    }

	});

