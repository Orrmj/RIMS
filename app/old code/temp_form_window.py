import sys
import datetime
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class CategoryWindow(qtw.QWidget):
    """A basic dialog to demonstrate inter-widget communication"""

    # when submitted, we'll emit this signal
    # with the entered string
    
    submitted = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__(None, modal=True)

        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(
            qtw.QLabel('Please enter a new catgory name:')
            )
        self.category_entry = qtw.QLineEdit()
        self.layout().addWidget(self.category_entry)

        self.submit_btn = qtw.QPushButton(
            'Submit',
            clicked=self.onSubmit
            )
        self.layout().addWidget(self.submit_btn)
        self.cancel_btn = qtw.QPushButton(
            'Cancel',
            # Errata:  The book contains this line:
            #clicked=self.destroy
            # It should call self.close instead, like so:
            clicked=self.close
            )
        self.layout().addWidget(self.cancel_btn)
        self.show()

    @qtc.pyqtSlot()
    def onSubmit(self):
        if self.category_entry.text():
            self.submitted.emit(self.category_entry.text())
        self.close()

class ChoiceSpinBox(qtw.QSpinBox):
    """A spinbox for selecting choices."""

    def __init__(self, choices, *args, **kwargs):
        self.choices = choices
        super().__init__(
            *args,
            maximum=len(self.choices) - 1,
            minimum=0,
            **kwargs
        )

    def valuefromText(self, text):
        return self.choices.index(text)

    def textfromValue(self, value):
        try:
            return self.choices[value]
        except IndexError:
            return '!Error!'

    def validate(self, string, index):
        if string in self.choices:
            state = qtg.QValidator.Acceptable
        elif any([v.startswith(string) for v in self.choices]):
            state = qtg.QValidator.intermediate
        else:
            state = qtg.QValidator.Invalid
        return (state, string, index)

class FormWindow(qtw.QWidget):

    submitted = qtc.pyqtSignal([str], [int, str])

    #settings = {'show_warnings': True}
    settings = qtc.QSettings('Alan D Moore', 'text editor')

    def __init__(self):
        super().__init__()
        
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('4.3 – Application Form GUI')
        self.formWidgets()

        self.show()
    
    def formWidgets(self):
        """
        Create widgets that will be used in the application form. 
        """

        # Combo Box Lists
        list_yes_no = ['Yes', 'No']
        list_yes_no_na = ['Yes', 'No', 'N/A']
        list_condition = ['Good', 'Fair', 'Poor']
        list_inspection_details_gcws_type = ['Active','Passive']
        list_inspection_details_grade_crossing_type = ['Public', 'Private (CTA 102-Type)', 'Private (CTA 103-Type)']
        list_inspection_details_track_type = ['Mainline', 'Industrial Spur', 'Mainline Spur', 'Yard, Other']
        list_inspection_details_province = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'ON', 'QC', 'SK', 'YT']
        list_inspection_details_reason_for_assessment = [
            "Periodic Assessment",
            "A Significant Change in Infrastructure",
            "Whistle Cessation",
            "2+ Fatal Collisions in 5-Year Period",
            "Other Collision Experience (see below)",
            "Receipt of a notice from a Railway Company, under Section 3 of the Notice of Railway Works Regulations. Ref. (GCR 12.(2))",
            "A change in the design vehicle and the sightlines at the grade crossing, which must meet the requirements in Section 20 of the GCR. Ref. (GCR 13 GCR 28.(c))",
            "An increase in the design speed of the road crossing, which will result in a change to the road approach's classification as set out in column B of the Table 10-2 of the Grade Crossings Standards (GCS). Ref. (GCR 13 GCR 28.(d))",
            "The location, gradient or crossing angle of a grade crossing has changed, and Articles 6 and 11 of the GCS must be applied in a manner that improves the overall safety of the grade crossing. Ref. (GCR 13 GCR 88.(1))",
            "An increase of the absolute gradient of a road approach to an existing grade crossing which meets the standards set out in Article 6.3 of the GCS. Ref. (GCR 13 GCR 88.(2))",
            "The number or width of traffic lanes of a road approach increases, or a shoulder is added or a shoulder's width is increased. The grade crossing must meet the standards set out in Articles 5.1 and 6.4 of the GCS. Ref. (GCR 13 GCR 89)",
            "A traffic signal is installed at a grade crossing that corresponds to the specifications set out in Article 19.1 of the GCS, the warning system must be interconnected with the traffic signal, and the interconnection must meet the standards set out in Articles 19.2 to 19.4 of the GCS. Ref. (GCR 13 GCR 90)",
            "A change in the design vehicle, which has resulted in a change to the period of time that the warning system must operate, before railway equipment reaches the crossing surface and therefore must meet the standards set out in Article 16.1 of the GCS. Ref. (GCR 13 GCR 91)",
            "Receipt of a notice from a Road Authority under Section 3 of the Notice of Railway Works Regulations. Ref. (GCR 4.(2))",
            "A line of railway is added within the sightlines of the grade crossing and the sightlines must meet the requirements in Section 20 of the GCR. Ref. (GCR 5 – GCR 28.(a))"
            "There is a change in the class of track referred to in column 1 of the table in article 7.1.2 of the Grade Crossing Standards (GCS),  taking into account the maximum allowable operating speeds set out in column 2 or 3 of that table. Sightlines at the grade crossing must meet the requirements in Section 20 of the GCR. Ref. (GCR 5 – GCR 28.(b))",
            "A new warning system is installed at a grade crossing and must meet the applicable standards set out in Articles 12 to 16 of the GCS. Ref. (GCR 5 – GCR 87.(1))",
            "A component of a warning system is modified or installed and must meet the applicable standards set out in Articles 12 and 16 of the GCS. Ref. (GCR 5 – GCR 87.(2))",
            "A new installation of a warning system, or the modification or installation of a component of a warning system which results from an increase in the railway design speed. The warning system or component must meet the applicable standards set out in Articles 12 and 16 of the GCS before the increase in the railway design speed takes effect. Ref. (GCR 5 – GCR 87.(3))"
            ]
        list_general_info_road_classification = ['Rural Local Undivided', 'Rural Collector Undivided',
            'Rural Collector Divided', 'Rural Arterial Undivided', 'Rural Arterial Divided', 'Rural Freeway Divided',
            'Urban Local Undivided', 'Urban Collector Undivided', 'Urban Collector Divided', 'Urban Arterial Undivided',
            'Urban Arterial Divided', 'Private Road', 'Pedestrian Crossing']
        list_general_info_observe_surrounding_land_use = ['Farm', 'Residential', 'Recreational', 'Industrial', 'Commercial']
        list_design_road_design_vehicle_type = ['Passenger Cars, Vans, and Pickups', 'Light Single-Unit Trucks',
            'Medium Single-Unit Trucks', 'Heavy Single-Unit Trucks', 'WB-19 Tractor-Semitrailers', 
            'WB-20 Tractor-Semitrailers', 'A-Train Doubles (ATD)', 'B-Train Doubles', 'Standard Single-Unit Buses (B-12)',
            'Articulated Buses (A-Bus)', 'Intercity Buses (I-Bus)', 'Pedestrian Only']
        list_grade_crossing_surface_observe_material = ['Timber', 'Asphalt', 'Asphalt and Flange', 
            'Concrete', 'Concrete and Rubber', 'Rubber', 'Metal', 'Unconsolidated', 'Other']
        list_grade_crossing_surface_observe_road_approach_surface_type = ['Asphalt', 'Concrete', 'Gravel']
        list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = ['Not Interconnected', 'Advance Preemption', 'Simultaneous Preemption']
                
        # INSPECTION DETAILS
        #Group TextBoxes
        input_inspection_details_assessment_team = qtw.QTextEdit()
        
        '''
        #Group DatePicker
        input_inspection_details_date_assessment = qtw.QDatetimeEdit(
            self,
            date=datetime.date.today(),
            calendarPopup=True,
            displayFormat='yyyy-MM-dd'
        )
        '''

        #Group LineEdits
        input_inspection_details_crossing_location = qtw.QLineEdit() 
        input_inspection_details_latitude = qtw.QLineEdit() 
        input_inspection_details_location_number = qtw.QLineEdit() 
        input_inspection_details_longitude = qtw.QLineEdit() 
        input_inspection_details_municipality = qtw.QLineEdit() 
        input_inspection_details_road_name = qtw.QLineEdit() 
        input_inspection_details_road_number = qtw.QLineEdit() 
        input_inspection_details_spur_mile = qtw.QLineEdit() 
        input_inspection_details_spur_name = qtw.QLineEdit() 
        input_inspection_details_subdivision_mile = qtw.QLineEdit() 

        #Group ComboBoxes
        input_inspection_details_gcws_type = qtw.QComboBox()
        input_inspection_details_gcws_type.addItems(list_inspection_details_gcws_type)

        input_inspection_details_grade_crossing_type = qtw.QComboBox()
        input_inspection_details_grade_crossing_type.addItems(list_inspection_details_grade_crossing_type)

        input_inspection_details_province = qtw.QComboBox()
        input_inspection_details_province.addItems(list_inspection_details_province)

        input_inspection_details_railway_authority = qtw.QComboBox()
        #TODO create and add railway authority list 

        input_inspection_details_reason_for_assessment = qtw.QComboBox()
        input_inspection_details_reason_for_assessment.addItems(list_inspection_details_reason_for_assessment)
        
        input_inspection_details_road_authority = qtw.QComboBox()
        #TODO create and add road authority list 

        input_inspection_details_subdivision_name = qtw.QComboBox()
        #TODO create and add subdivision list 

        input_inspection_details_track_type = qtw.QComboBox()
        input_inspection_details_track_type.addItems(list_inspection_details_track_type)

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        input_collision_history_comments = qtw.QTextEdit()

        #Group LineEdits
        input_collision_history_fatal_injury = qtw.QLineEdit() 
        input_collision_history_fatalities = qtw.QLineEdit() 
        input_collision_history_personal_injuries = qtw.QLineEdit() 
        input_collision_history_personal_injury = qtw.QLineEdit() 
        input_collision_history_property_damage = qtw.QLineEdit() 
        input_collision_history_total_5_year_period = qtw.QLineEdit() 

        # GENERAL INFORMATION
        #Group TextEdits
        input_general_info_comments = qtw.QTextEdit()

        #Group LineEdits
        input_general_info_observe_special_buildings = qtw.QLineEdit() 
        input_general_info_rail_max_railway_operating_speed_freight = qtw.QLineEdit() 
        input_general_info_rail_max_railway_operating_speed_passenger = qtw.QLineEdit() 
        input_general_info_rail_no_trains_per_day_freight = qtw.QLineEdit() 
        input_general_info_rail_no_trains_per_day_passengers = qtw.QLineEdit() 
        input_general_info_rail_railway_design_speed = qtw.QLineEdit() 
        input_general_info_road_aadt_current = qtw.QLineEdit() 
        input_general_info_road_aadt_forecast = qtw.QLineEdit() 
        input_general_info_road_aadt_year_current = qtw.QLineEdit() 
        input_general_info_road_aadt_year_forecasted = qtw.QLineEdit() 
        input_general_info_road_cyclist_per_day = qtw.QLineEdit() 
        input_general_info_road_no_traffic_lanes_bidirectional = qtw.QLineEdit() 
        input_general_info_road_no_traffic_lanes_northbound_or_eastbound = qtw.QLineEdit() 
        input_general_info_road_no_traffic_lanes_southbound_or_westbound = qtw.QLineEdit() 
        input_general_info_road_other_users = qtw.QLineEdit() 
        input_general_info_road_other_users_daily_users = qtw.QLineEdit() 
        input_general_info_road_pedestrians_per_day = qtw.QLineEdit() 
        input_general_info_road_speed_design = qtw.QLineEdit() 
        input_general_info_road_speed_posted = qtw.QLineEdit() 

        #Group ComboBoxes
        input_general_info_observe_roadway_illumination = qtw.QComboBox()
        input_general_info_observe_roadway_illumination.addItems(list_yes_no)

        input_general_info_observe_surrounding_land_use = qtw.QComboBox()
        input_general_info_observe_surrounding_land_use.addItems(list_general_info_observe_surrounding_land_use)

        input_general_info_rail_train_switching = qtw.QComboBox()
        input_general_info_rail_train_switching.addItems(list_yes_no)
        
        input_general_info_road_assistive_pedestrian_devices = qtw.QComboBox()
        input_general_info_road_assistive_pedestrian_devices.addItems(list_yes_no)

        input_general_info_road_classification = qtw.QComboBox()
        input_general_info_road_classification.addItems(list_general_info_road_classification)
        
        input_general_info_road_dangerous_goods_route = qtw.QComboBox()
        input_general_info_road_dangerous_goods_route.addItems(list_yes_no)

        input_general_info_road_school_bus_route = qtw.QComboBox()
        input_general_info_road_school_bus_route.addItems(list_yes_no)


        input_general_info_road_seasonal_volume_fluctuations = qtw.QComboBox()
        input_general_info_road_seasonal_volume_fluctuations.addItems(list_yes_no)

        input_general_info_road_sidewalks = qtw.QComboBox()
        input_general_info_road_sidewalks.addItems(list_yes_no)

        #Group Labels
        #TODO input_general_info_rail_no_tracks_total = pass
        #TODO input_general_info_rail_no_trains_per_day_total = pass
        #TODO input_general_info_road_no_traffic_lanes_total = pass

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        input_design_comments = qtw.QTextEdit()

        #Group LineEdits
        input_design_measure_adjacent_track_clearance_distance = qtw.QLineEdit() 
        input_design_measure_adjacent_track_separation_distance = qtw.QLineEdit() 
        input_design_measure_clearance_distance_pedestrian = qtw.QLineEdit() 
        input_design_measure_clearance_distance_vehicle = qtw.QLineEdit() 
        input_design_road_max_approach_grade_within_s = qtw.QLineEdit() 

        #Group ComboBoxes
        input_design_observe_field_acceleration_times_exceed_td = qtw.QComboBox()
        input_design_observe_field_acceleration_times_exceed_td.addItems(list_yes_no)

        input_design_road_design_vehicle_type = qtw.QComboBox()
        input_design_road_design_vehicle_type.addItems(list_design_road_design_vehicle_type)

        #Group Labels
        #TODO input_design_calculate_adjacent_track_clearance_time = pass
        #TODO input_design_calculate_clearance_time_crossing_pedestrian_input_design_check = pass
        #TODO input_design_calculate_clearance_time_crossing_vehicle_input_design_check = pass
        #TODO input_design_calculate_clearance_time_gate_arm_ssd = pass
        #TODO input_design_calculate_clearance_time_gate_arm_stop = pass
        #TODO input_design_calculate_vehicle_travel_distance = pass
        #TODO input_design_input_reaction_time = pass
        #TODO input_design_lookup_input_design_vehicle_class = pass
        #TODO input_design_lookup_input_design_vehicle_length = pass
        #TODO input_design_lookup_grade_adjustment_factor = pass
        #TODO input_design_lookup_vehicle_departure_time_crossing = pass
        #TODO input_design_lookup_vehicle_departure_time_gate_arm_clearance = pass
        
        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        input_location_of_grade_crossing_comments = qtw.QTextEdit()

        #Group LineEdits
        input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = qtw.QLineEdit() 
        input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = qtw.QLineEdit() 
        input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = qtw.QLineEdit() 
        input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = qtw.QLineEdit() 
        input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = qtw.QLineEdit() 
        input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = qtw.QLineEdit() 

        #group ComboBoxes
        input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = qtw.QComboBox()
        input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk.addItems(list_yes_no)

        input_location_of_grade_crossing_queue_condition = qtw.QComboBox()
        input_location_of_grade_crossing_queue_condition.addItems(list_yes_no)

        input_location_of_grade_crossing_visibility_of_warning_lights = qtw.QComboBox()
        input_location_of_grade_crossing_queue_condition.addItems(list_yes_no)
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        input_grade_crossing_surface_comments = qtw.QTextEdit()

        #Group LineEdits
        input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_crossing_surface_width = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_flangeway_depth = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_flangeway_width = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_road_surface_median_width = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_side_grinding_depth = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_side_grinding_width = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = qtw.QLineEdit() 
        input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = qtw.QLineEdit() 

        #Group ComboBoxes
        input_grade_crossing_surface_observe_crossing_smoothness = qtw.QComboBox()
        input_grade_crossing_surface_observe_crossing_smoothness.addItems(list_yes_no)

        input_grade_crossing_surface_observe_crossing_surface_condition = qtw.QComboBox()
        input_grade_crossing_surface_observe_crossing_smoothness.addItems(list_condition)

        input_grade_crossing_surface_observe_material = qtw.QComboBox()
        input_grade_crossing_surface_observe_material.addItems(list_grade_crossing_surface_observe_material)

        input_grade_crossing_surface_observe_road_approach_surface_condition = qtw.QComboBox()
        input_grade_crossing_surface_observe_road_approach_surface_condition.addItems(list_condition)

        input_grade_crossing_surface_observe_road_approach_surface_type = qtw.QComboBox()
        input_grade_crossing_surface_observe_road_approach_surface_type.addItems(list_grade_crossing_surface_observe_road_approach_surface_type)

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        input_road_geometry_comments = qtw.QTextEdit()

        #Group LineEdits
        input_road_geometry_measure_railway_cross_slope = qtw.QLineEdit() 
        input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = qtw.QLineEdit() 
        input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = qtw.QLineEdit() 
        input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = qtw.QLineEdit() 
        input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = qtw.QLineEdit() 
        input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = qtw.QLineEdit() 
        input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = qtw.QLineEdit() 
        input_road_geometry_rail_superelevation_n_or_e_approach = qtw.QLineEdit() 
        input_road_geometry_rail_superelevation_s_or_w_approach = qtw.QLineEdit() 
        input_road_geometry_road_crossing_angle = qtw.QLineEdit() 
        input_road_geometry_road_general_approach_grade_n_or_e_approach = qtw.QLineEdit() 
        input_road_geometry_road_general_approach_grade_s_or_w_approach = qtw.QLineEdit() 

        #Group ComboBoxes
        input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = qtw.QComboBox()
        input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach.addItems(list_yes_no)

        input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = qtw.QComboBox()
        input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach.addItems(list_yes_no)

        input_road_geometry_observe_low_bed_truck_condition = qtw.QComboBox()
        input_road_geometry_observe_low_bed_truck_condition.addItems(list_yes_no)

        input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = qtw.QComboBox()
        input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach.addItems(list_yes_no)

        input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = qtw.QComboBox()
        input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach.addItems(list_yes_no)
       
        #Group Labels
        #TODO input_road_geometry_lookup_gradient_difference = pass
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        input_sightlines_comments = qtw.QTextEdit()
        
        #Group LineEdits
        input_sightlines_measure_dssd_actual_n_or_e_approach_left = qtw.QLineEdit() 
        input_sightlines_measure_dssd_actual_n_or_e_approach_right = qtw.QLineEdit() 
        input_sightlines_measure_dssd_actual_s_or_w_approach_left = qtw.QLineEdit() 
        input_sightlines_measure_dssd_actual_s_or_w_approach_right = qtw.QLineEdit() 
        input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = qtw.QLineEdit() 
        input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = qtw.QLineEdit() 
        input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = qtw.QLineEdit() 
        input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = qtw.QLineEdit() 
        input_sightlines_measure_ssd_actual_n_or_e_approach = qtw.QLineEdit() 
        input_sightlines_measure_ssd_actual_s_or_w_approach = qtw.QLineEdit() 

        #Group ComboBoxes
        input_sightlines_observe_sightline_obstructions = qtw.QComboBox()
        input_sightlines_observe_sightline_obstructions.addItems(list_yes_no)

        #Group Labels
        #TODO input_sightlines_calculate_dssd_vehicle_min_ft = pass
        #TODO input_sightlines_calculate_dssd_vehicle_min_m = pass
        #TODO input_sightlines_calculate_dstopped_pedestrian_min_ft = pass
        #TODO input_sightlines_calculate_dstopped_pedestrian_min_m = pass
        #TODO input_sightlines_calculate_dstopped_vehicle_min_ft = pass
        #TODO input_sightlines_calculate_dstopped_vehicle_min_m = pass
        #TODO input_sightlines_lookup_ssd_minimum_n_or_e_approach = pass
        #TODO input_sightlines_lookup_ssd_minimum_s_or_w_approach = pass

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE input_signs_and_markings_advisory_speed_comments = pass
        #DELETE input_signs_and_markings_comments = pass
        #DELETE input_signs_and_markings_emergency_notification_comments = pass
        #DELETE input_signs_and_markings_number_of_tracks_comments = pass
        #DELETE input_signs_and_markings_railway_crossing_ahead_comments = pass
        #DELETE input_signs_and_markings_railway_crossing_comments = pass
        #DELETE input_signs_and_markings_stop_comments = pass
        #DELETE input_signs_and_markings_stop_sign_ahead_comments = pass

        #Group LineEdits
        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = qtw.QLineEdit() 
        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = qtw.QLineEdit() 
        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = qtw.QLineEdit() 
        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = qtw.QLineEdit() 
        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = qtw.QLineEdit() 
        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = qtw.QLineEdit() 
        input_signs_and_markings_stop_n_or_e_approach_height = qtw.QLineEdit() 
        input_signs_and_markings_stop_n_or_e_approach_location_from_rail = qtw.QLineEdit() 
        input_signs_and_markings_stop_n_or_e_approach_location_from_road = qtw.QLineEdit() 
        input_signs_and_markings_stop_s_or_w_approach_height = qtw.QLineEdit() 
        input_signs_and_markings_stop_s_or_w_approach_location_from_rail = qtw.QLineEdit() 
        input_signs_and_markings_stop_s_or_w_approach_location_from_road = qtw.QLineEdit() 
        input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = qtw.QLineEdit() 
        input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = qtw.QLineEdit() 
        input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = qtw.QLineEdit() 
        input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = qtw.QLineEdit() 
        input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = qtw.QLineEdit() 
        input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = qtw.QLineEdit() 

        #Group ComboBoxes
        input_signs_and_markings_advisory_speed_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_advisory_speed_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = qtw.QComboBox()
        input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20.addItems(list_yes_no_na)

        input_signs_and_markings_advisory_speed_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_advisory_speed_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = qtw.QComboBox()
        input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20.addItems(list_yes_no_na)

        input_signs_and_markings_dividing_lines_present = qtw.QComboBox()
        input_signs_and_markings_dividing_lines_present.addItems(list_yes_no)

        input_signs_and_markings_emergency_notification_n_or_e_approach_condition = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_n_or_e_approach_condition.addItems(list_condition)

        input_signs_and_markings_emergency_notification_n_or_e_approach_legible = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_n_or_e_approach_legible.addItems(list_yes_no_na)

        input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation = qtw.QComboBox()
        input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation.addItems(list_yes_no_na)

        input_signs_and_markings_emergency_notification_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_emergency_notification_s_or_w_approach_condition = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_s_or_w_approach_condition.addItems(list_condition)

        input_signs_and_markings_emergency_notification_s_or_w_approach_legible = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_s_or_w_approach_legible.addItems(list_yes_no_na)

        input_signs_and_markings_emergency_notification_s_or_w_approach_orientation = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_s_or_w_approach_orientation.addItems(list_yes_no_na)

        input_signs_and_markings_emergency_notification_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_emergency_notification_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = qtw.QComboBox()
        input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b.addItems(list_yes_no_na)

        input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = qtw.QComboBox()
        input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c.addItems(list_yes_no_na)

        input_signs_and_markings_number_of_tracks_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_number_of_tracks_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = qtw.QComboBox()
        input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b.addItems(list_yes_no_na)

        input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = qtw.QComboBox()
        input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c.addItems(list_yes_no_na)

        input_signs_and_markings_number_of_tracks_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_number_of_tracks_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_per_mutcd = qtw.QComboBox()
        input_signs_and_markings_per_mutcd.addItems(list_yes_no)

        input_signs_and_markings_posted_speed_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_posted_speed_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_posted_speed_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_posted_speed_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation.addItems(list_yes_no_na)

        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation.addItems(list_yes_no_na)

        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a.addItems(list_yes_no)


        input_signs_and_markings_railway_crossing_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a.addItems(list_yes_no)

        input_signs_and_markings_railway_crossing_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_railway_crossing_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_sidewalks_present = qtw.QComboBox()
        input_signs_and_markings_sidewalks_present.addItems(list_yes_no)

        input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = qtw.QComboBox()
        input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4.addItems(list_yes_no_na)

        input_signs_and_markings_stop_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_stop_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_stop_n_or_e_approach_same_post = qtw.QComboBox()
        input_signs_and_markings_stop_n_or_e_approach_same_post.addItems(list_yes_no_na)

        input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = qtw.QComboBox()
        input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4.addItems(list_yes_no_na)

        input_signs_and_markings_stop_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_stop_s_or_w_approach_present.addItems(list_yes_no)

        input_signs_and_markings_stop_s_or_w_approach_same_post = qtw.QComboBox()
        input_signs_and_markings_stop_s_or_w_approach_same_post.addItems(list_yes_no_na)

        input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = qtw.QComboBox()
        input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present.addItems(list_yes_no)

        input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = qtw.QComboBox()
        input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present.addItems(list_yes_no)

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #Group Labels
        #TODO input_gcws_warrant_private_9_3_1 = pass
        #TODO input_gcws_warrant_private_9_3_2_a = pass
        #TODO input_gcws_warrant_private_9_3_2_b = pass
        #TODO input_gcws_warrant_private_9_3_2_c = pass
        #TODO input_gcws_warrant_public_9_1_a = pass
        #TODO input_gcws_warrant_public_9_1_b = pass
        #TODO input_gcws_warrant_public_9_1_c = pass
        #TODO input_gcws_warrant_public_9_1_d_i = pass
        #TODO input_gcws_warrant_public_9_1_d_ii = pass
        #TODO input_gcws_warrant_public_9_1_d_iii = pass
        #TODO input_gcws_warrant_sidewalk_9_5 = pass
        #TODO input_gcws_warrants_comments = pass

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = qtw.QLineEdit() 
        input_gcws_measure_warning_device_n_or_e_approach_distance_from_road = qtw.QLineEdit() 
        input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = qtw.QLineEdit() 
        input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = qtw.QLineEdit() 
        input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = qtw.QLineEdit() 
        input_gcws_measure_warning_device_s_or_w_approach_distance_from_road = qtw.QLineEdit() 
        input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = qtw.QLineEdit() 
        input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = qtw.QLineEdit() 
        input_gcws_rail_crossing_warning_time_actual = qtw.QLineEdit() 

        #Group ComboBox
        input_gcws_observe_bell_if_sidewalk = qtw.QComboBox()
        input_gcws_observe_bell_if_sidewalk.addItems(list_yes_no)

        input_gcws_observe_bells_condition = qtw.QComboBox()
        input_gcws_observe_bells_condition.addItems(list_condition)

        input_gcws_observe_bells_n_or_e_approach = qtw.QComboBox()
        input_gcws_observe_bells_n_or_e_approach.addItems(list_yes_no)

        input_gcws_observe_bells_s_or_w_approach = qtw.QComboBox()
        input_gcws_observe_bells_s_or_w_approach.addItems(list_yes_no)

        input_gcws_observe_cantilever_lights_condition = qtw.QComboBox()
        input_gcws_observe_cantilever_lights_condition.addItems(list_condition)

        input_gcws_observe_cantilever_lights_n_or_e_approach = qtw.QComboBox()
        input_gcws_observe_cantilever_lights_n_or_e_approach.addItems(list_yes_no)

        input_gcws_observe_cantilever_lights_s_or_w_approach = qtw.QComboBox()
        input_gcws_observe_cantilever_lights_s_or_w_approach.addItems(list_yes_no)

        input_gcws_observe_gates_condition = qtw.QComboBox()
        input_gcws_observe_gates_condition.addItems(list_condition)

        input_gcws_observe_gates_n_or_e_approach = qtw.QComboBox()
        input_gcws_observe_gates_n_or_e_approach.addItems(list_yes_no)

        input_gcws_observe_gates_s_or_w_approach = qtw.QComboBox()
        input_gcws_observe_gates_s_or_w_approach.addItems(list_yes_no)

        input_gcws_observe_gcws_limited_use_with_walk_light_assembly = qtw.QComboBox()
        input_gcws_observe_gcws_limited_use_with_walk_light_assembly.addItems(list_yes_no_na)

        input_gcws_observe_gcws_limited_use_without_walk_light_assembly = qtw.QComboBox()
        input_gcws_observe_gcws_limited_use_without_walk_light_assembly.addItems(list_yes_no_na)

        input_gcws_observe_light_units_condition = qtw.QComboBox()
        input_gcws_observe_light_units_condition.addItems(list_condition)

        input_gcws_observe_light_units_n_or_e_approach = qtw.QComboBox()
        input_gcws_observe_light_units_n_or_e_approach.addItems(list_yes_no)

        input_gcws_observe_light_units_s_or_w_approach = qtw.QComboBox()
        input_gcws_observe_light_units_s_or_w_approach.addItems(list_yes_no)

        input_gcws_observe_warning_time_consistency = qtw.QComboBox()
        input_gcws_observe_warning_time_consistency.addItems(list_yes_no_na)
        
        input_gcws_observe_warning_time_consistency_reduced_speed = qtw.QComboBox()
        input_gcws_observe_warning_time_consistency_reduced_speed.addItems(list_yes_no_na)

        input_gcws_rail_cut_out_circuit_requirements = qtw.QComboBox()
        input_gcws_rail_cut_out_circuit_requirements.addItems(list_yes_no_na)

        input_gcws_rail_directional_stick_circuit_requirements = qtw.QComboBox()
        input_gcws_rail_directional_stick_circuit_requirements.addItems(list_yes_no_na)

        input_gcws_rail_self_diagnostic = qtw.QComboBox()
        input_gcws_rail_self_diagnostic.addItems(list_yes_no_na)

        #Group Labels
        #TODO input_gcws_rail_design_approach_warning_time = pass
        #TODO input_gcws_rail_design_warning_time_adjacent_crossing = pass
        #TODO input_gcws_rail_design_warning_time_clearance_distance = pass
        #TODO input_gcws_rail_design_warning_time_departure_time_pedestrian = pass
        #TODO input_gcws_rail_design_warning_time_departure_time_vehicle = pass
        #TODO input_gcws_rail_design_warning_time_gate_arm_clearance = pass
        #TODO input_gcws_rail_design_warning_time_preemption = pass
        #TODO input_gcws_rail_design_warning_time_ssd = pass

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        input_light_units_comments = qtw.QTextEdit()

        #Group LineEdits
        input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_n_or_e_approach_dl = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_n_or_e_approach_dr = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_n_or_e_approach_height = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_s_or_w_approach_dl = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_s_or_w_approach_dr = qtw.QLineEdit() 
        input_light_units_measure_cantilevers_s_or_w_approach_height = qtw.QLineEdit() 
        input_light_units_measure_n_or_e_approach_height = qtw.QLineEdit() 
        input_light_units_measure_s_or_w_approach_height = qtw.QLineEdit() 

        #Group ComboBoxes
        input_light_units_observe_cantilevers_n_or_e_approach_per_fig_12_3 = qtw.QComboBox()
        input_light_units_observe_cantilevers_n_or_e_approach_per_fig_12_3.addItems(list_yes_no_na)

        input_light_units_observe_n_or_e_approach_per_fig_12_1 = qtw.QComboBox()
        input_light_units_observe_n_or_e_approach_per_fig_12_1.addItems(list_yes_no_na)

        input_light_units_observe_sidewalks_n_or_e_approach = qtw.QComboBox()
        input_light_units_observe_sidewalks_n_or_e_approach.addItems(list_yes_no_na)

        input_light_units_observe_sidewalks_s_or_w_approach = qtw.QComboBox()
        input_light_units_observe_sidewalks_s_or_w_approach.addItems(list_yes_no_na)

        input_light_units_observe_supplemental_lights_n_or_e_approach = qtw.QComboBox()
        input_light_units_observe_supplemental_lights_n_or_e_approach.addItems(list_yes_no_na)

        input_light_units_observe_supplemental_lights_s_or_w_approach = qtw.QComboBox()
        input_light_units_observe_supplemental_lights_s_or_w_approach.addItems(list_yes_no_na)

        input_light_units_observe_visibility_back_lights_n_or_e_approach = qtw.QComboBox()
        input_light_units_observe_visibility_back_lights_n_or_e_approach.addItems(list_yes_no_na)

        input_light_units_observe_visibility_back_lights_s_or_w_approach = qtw.QComboBox()
        input_light_units_observe_visibility_back_lights_s_or_w_approach.addItems(list_yes_no_na)

        input_light_units_observe_visibility_front_lights_n_or_e_approach = qtw.QComboBox()
        input_light_units_observe_visibility_front_lights_n_or_e_approach.addItems(list_yes_no_na)

        input_light_units_observe_visibility_front_lights_s_or_w_approach = qtw.QComboBox()
        input_light_units_observe_visibility_front_lights_s_or_w_approach.addItems(list_yes_no_na)

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        input_gates_gcws_comments = qtw.QTextEdit()

        #Group LineEdits
        input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = qtw.QLineEdit() 
        input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = qtw.QLineEdit() 
        input_gates_gcws_measure_gate_ascent_time = qtw.QLineEdit() 
        input_gates_gcws_measure_gate_descent_time = qtw.QLineEdit() 
        input_gates_gcws_rail_gate_arm_delay_time_design = qtw.QLineEdit() 
        input_gates_gcws_rail_gate_arm_descent_time_design = qtw.QLineEdit() 
        input_gates_gcws_rail_inner_gate_arm_delay_time_design = qtw.QLineEdit() 

        #Group Labels
        #TODO input_gates_gcws_calculate_gate_arm_clearance_time_recommended = pass
        #TODO input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = pass

        #Group ComboBoxes
        input_gates_gcws_observe_gate_arm_rest = qtw.QComboBox()
        input_gates_gcws_observe_gate_arm_rest.addItems(list_yes_no_na)

        input_gates_gcws_observe_gate_ascent_time = qtw.QComboBox()
        input_gates_gcws_observe_gate_ascent_time.addItems(list_yes_no_na)

        input_gates_gcws_observe_gate_descent_time = qtw.QComboBox()
        input_gates_gcws_observe_gate_descent_time.addItems(list_yes_no_na)

        input_gates_gcws_observe_gate_strips_n_or_e_approach = qtw.QComboBox()
        input_gates_gcws_observe_gate_strips_n_or_e_approach.addItems(list_yes_no_na)

        input_gates_gcws_observe_gate_strips_s_or_w_approach = qtw.QComboBox()
        input_gates_gcws_observe_gate_strips_s_or_w_approach.addItems(list_yes_no_na)

        input_gates_gcws_observe_per_fig_12_2 = qtw.QComboBox()
        input_gates_gcws_observe_per_fig_12_2.addItems(list_yes_no_na)

        #Group Labels
        #TODO input_gates_gcws_warrant_private_9_4_1_a = pass
        #TODO input_gates_gcws_warrant_private_9_4_1_b = pass
        #TODO input_gates_gcws_warrant_private_9_4_1_c = pass
        #TODO input_gates_gcws_warrant_public_9_2_1_a = pass
        #TODO input_gates_gcws_warrant_public_9_2_1_b = pass
        #TODO input_gates_gcws_warrant_public_9_2_1_c = pass
        #TODO input_gates_gcws_warrant_public_9_2_1_d = pass
        #TODO input_gates_gcws_warrant_public_9_2_1_e = pass
        #TODO input_gates_gcws_warrant_sidewalk_9_6 = pass

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        input_aawd_comments = qtw.QTextEdit()

        #Group LineEdits
        input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = qtw.QLineEdit() 
        input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = qtw.QLineEdit() 

        #Group ComboBoxes
        input_aawd_observe_present_n_or_e_approach = qtw.QComboBox()
        input_aawd_observe_present_n_or_e_approach.addItems(list_yes_no)

        input_aawd_observe_present_s_or_w_approach = qtw.QComboBox()
        input_aawd_observe_present_s_or_w_approach.addItems(list_yes_no)

        input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = qtw.QComboBox()
        input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = qtw.QComboBox()
        input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach.addItems(list_yes_no_na)

        #Group Labels
        #TODO input_aawd_calculate_advance_activation_time_design_n_or_e_approach = pass
        #TODO input_aawd_calculate_advance_activation_time_design_s_or_w_approach = pass
        #TODO input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = pass
        #TODO input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = pass
        #TODO input_aawd_warrant_gcr_lookup_road_classification = pass
        #TODO input_aawd_warrant_gcr_observe_environmental_condition = pass
        #TODO input_aawd_warrant_gcr_observe_sightline_Obstruction = pass
        #TODO input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = pass
        #TODO input_aawd_warrant_mutcd_lookup_significant_road_downgrade = pass

        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals_comments = qtw.QTextEdit()
    
        #Group LineEdits
        input_preemption_of_traffic_signals_road_preemption_warning_time_actual = qtw.QLineEdit() 
        input_preemption_of_traffic_signals_road_preemption_warning_time_design = qtw.QLineEdit() 

        #Group CombBoxes
        input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles.addItems(list_yes_no)

        input_preemption_of_traffic_signals_observe_known_queuing_issues = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_known_queuing_issues.addItems(list_yes_no)

        input_preemption_of_traffic_signals_observe_pedestrian_accommodation = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_pedestrian_accommodation.addItems(list_yes_no_na)

        input_preemption_of_traffic_signals_observe_queuing_condition = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_queuing_condition.addItems(list_yes_no)

        input_preemption_of_traffic_signals_observe_supplemental_signage = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_supplemental_signage.addItems(list_yes_no_na)

        input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate.addItems(list_yes_no_na)

        input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = qtw.QComboBox()
        input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals.addItems(list_yes_no_na)

        input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = qtw.QComboBox()
        input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type.addItems(list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)

        #Group DatePicker
        #TODO input_preemption_of_traffic_signals_road_date_Last_preemption_check = pass

        #Group Labels
        #TODO input_preemption_of_traffic_signals_lookup_proximity_condition = pass
        #TODO input_preemption_of_traffic_signals_lookup_required = pass

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        input_areas_without_train_whistling_comments = qtw.QTextEdit()

        #Group ComboBoxes
        input_areas_without_train_whistling_observe_for_stop_and_proceed = qtw.QComboBox()
        input_areas_without_train_whistling_observe_for_stop_and_proceed.addItems(list_yes_no_na)

        input_areas_without_train_whistling_observe_trespassing_area = qtw.QComboBox()
        input_areas_without_train_whistling_observe_trespassing_area.addItems(list_yes_no)

        input_areas_without_train_whistling_rail_anti_whistling_zone = qtw.QComboBox()
        input_areas_without_train_whistling_rail_anti_whistling_zone.addItems(list_yes_no)

        input_areas_without_train_whistling_rail_anti_whistling_zone_24_Hrs = qtw.QComboBox()
        input_areas_without_train_whistling_rail_anti_whistling_zone_24_Hrs.addItems(list_yes_no)

        #Group Labels
        #TODO input_areas_without_train_whistling_lookup_gcs_12_to_16 = pass
        #TODO input_areas_without_train_whistling_lookup_gcs_9_2 = pass
        #TODO input_areas_without_train_whistling_requirements_observe_table_D1 = pass
        

        ##################
        # Layout Objects #
        ##################
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # create a container widget
        container_inspection_details = qtw.QWidget(self)
        container_collision_history = qtw.QWidget(self)
        container_general_information = qtw.QWidget(self)
        container_design_considerations = qtw.QWidget(self)
        container_location_of_crossing = qtw.QWidget(self)
        container_crossing_surface = qtw.QWidget(self)
        container_road_geometry = qtw.QWidget(self)
        container_sightlines = qtw.QWidget(self)
        container_signs_and_pavement_markings = qtw.QWidget(self)
        container_gcws_warrants = qtw.QWidget(self)
        container_gcws = qtw.QWidget(self)
        container_gcws_lights = qtw.QWidget(self)
        container_gcws_gates = qtw.QWidget(self)
        container_aaws = qtw.QWidget(self)
        container_interconnection_traffic_signals = qtw.QWidget(self)
        container_whistle_cessation = qtw.QWidget(self)
        container_whistle_cessation = qtw.QWidget(self)
        
        # QFormLayout
        # create a form layout
        form_layout_inspection_details = qtw.QFormLayout()
        form_layout_collision_history = qtw.QFormLayout()
        form_layout_general_information = qtw.QFormLayout()
        form_layout_design_considerations = qtw.QFormLayout()
        form_layout_location_of_crossing = qtw.QFormLayout()
        form_layout_crossing_surface = qtw.QFormLayout()
        form_layout_road_geometry = qtw.QFormLayout()
        form_layout_sightlines = qtw.QFormLayout()
        form_layout_signs_and_pavement_markings = qtw.QFormLayout()
        form_layout_gcws_warrants = qtw.QFormLayout()
        form_layout_gcws = qtw.QFormLayout()
        form_layout_gcws_lights = qtw.QFormLayout()
        form_layout_gcws_gates = qtw.QFormLayout()
        form_layout_aaws = qtw.QFormLayout()
        form_layout_interconnection_traffic_signals = qtw.QFormLayout()
        form_layout_whistle_cessation = qtw.QFormLayout()
        
        #layout.setLayout(form_layout)
        container_inspection_details.setLayout(form_layout_inspection_details)        
        container_collision_history.setLayout(form_layout_collision_history)
        container_general_information.setLayout(form_layout_general_information)
        container_design_considerations.setLayout(form_layout_design_considerations)
        container_location_of_crossing.setLayout(form_layout_location_of_crossing)
        container_crossing_surface.setLayout(form_layout_crossing_surface)
        container_road_geometry.setLayout(form_layout_road_geometry)
        container_sightlines.setLayout(form_layout_sightlines)
        container_signs_and_pavement_markings.setLayout(form_layout_signs_and_pavement_markings)
        container_gcws_warrants.setLayout(form_layout_gcws_warrants)
        container_gcws.setLayout(form_layout_gcws)
        container_gcws_lights.setLayout(form_layout_gcws_lights)
        container_gcws_gates.setLayout(form_layout_gcws_gates)
        container_aaws.setLayout(form_layout_aaws)
        container_interconnection_traffic_signals.setLayout(form_layout_interconnection_traffic_signals)
        container_whistle_cessation.setLayout(form_layout_whistle_cessation)

        # layout container widgets - INSPECTION DETAILS
        #TODO form_layout_inspection_details.addRow('Date of Assessment:', input_inspection_details_date_assessment)
        form_layout_inspection_details.addRow('Assessment Team Members & Affiliations:', input_inspection_details_assessment_team)
        form_layout_inspection_details.addRow('Reason for Assessment:', input_inspection_details_reason_for_assessment)
        form_layout_inspection_details.addRow('Railway Authority:', input_inspection_details_railway_authority)
        form_layout_inspection_details.addRow('Crossing Location:', input_inspection_details_crossing_location)
        form_layout_inspection_details.addRow('Location Number:', input_inspection_details_location_number)
        form_layout_inspection_details.addRow('Subdivision Name:', input_inspection_details_subdivision_name)
        form_layout_inspection_details.addRow('Subdivision Mile:', input_inspection_details_subdivision_mile)
        form_layout_inspection_details.addRow('Spur Name:', input_inspection_details_spur_name)
        form_layout_inspection_details.addRow('Spur Mile:', input_inspection_details_spur_mile)
        form_layout_inspection_details.addRow('Type of Crossing:', input_inspection_details_grade_crossing_type)     
        form_layout_inspection_details.addRow('Type of Protection:', input_inspection_details_gcws_type)
        form_layout_inspection_details.addRow('Track Type:', input_inspection_details_track_type)
        form_layout_inspection_details.addRow('Road Authority:', input_inspection_details_road_authority)
        form_layout_inspection_details.addRow('Municipality:', input_inspection_details_municipality)
        form_layout_inspection_details.addRow('Road Name:', input_inspection_details_road_name)   
        form_layout_inspection_details.addRow('Road Number:', input_inspection_details_road_number)
        form_layout_inspection_details.addRow('Province:', input_inspection_details_province)     
        form_layout_inspection_details.addRow('Latitude:', input_inspection_details_latitude)
        form_layout_inspection_details.addRow('Longitude:', input_inspection_details_longitude)

        '''
        # layout container widgets - COLLISION HISTORY (5 YEAR PERIOD)
        form_layout_collision_history.addRow('Property Damage Collisions:', input_collision_history_property_damage)
        form_layout_collision_history.addRow('Personal Injury Collisions:', input_collision_history_personal_injury)
        form_layout_collision_history.addRow('Fatal Injury Collisions:', input_collision_history_fatal_injury)
        form_layout_collision_history.addRow('Total Collisions in the last 5 year period:', input_collision_history_total_5_year_period)
        form_layout_collision_history.addRow('Number of Persons Injured:', input_collision_history_fatalities)
        form_layout_collision_history.addRow('Number of Persons Killed:', input_collision_history_personal_injuries)
        form_layout_collision_history.addRow('Details of Collisions:', input_collision_history_comments)

        # layout container widgets - GENERAL INFORMATION
        form_layout_general_information.addRow('Maximum Freight Railway Operating Speed (mph)', input_general_info_rail_max_railway_operating_speed_freight)
        form_layout_general_information.addRow('Maximum Passenger Railway Operating Speed (mph)', input_general_info_rail_max_railway_operating_speed_passenger)
        form_layout_general_information.addRow('Railway Design Speed, VT (mph)', input_general_info_rail_railway_design_speed)
        form_layout_general_information.addRow('Freight Trains/Day:', input_general_info_rail_no_trains_per_day_freight)
        form_layout_general_information.addRow('Passenger Trains/Day:', input_general_info_rail_no_trains_per_day_passengers)
        #TODO form_layout_general_information.addRow('Total Trains/Day:', input_general_info_rail_no_trains_per_day_total)
        #TODO form_layout_general_information.addRow('Number of Tracks', input_general_info_rail_no_tracks_total)
        form_layout_general_information.addRow('Train Switching within Crossing Approaches?', input_general_info_rail_train_switching)
        form_layout_general_information.addRow('Road Crossing Design Speed (km/hr)', input_general_info_road_speed_design)
        form_layout_general_information.addRow('Road Posted Speed (km/hr)', input_general_info_road_speed_posted)
        form_layout_general_information.addRow('Current Average Annual Daily Traffic, AADT', input_general_info_road_aadt_current)
        form_layout_general_information.addRow('Year of Count:', input_general_info_road_aadt_year_current)
        form_layout_general_information.addRow('Forecasted Average Annual Daily Traffic, AADT', input_general_info_road_aadt_forecast)
        form_layout_general_information.addRow('Forecast Year:', input_general_info_road_aadt_year_forecasted)
        form_layout_general_information.addRow('Pedestrian Volume per Day', input_general_info_road_pedestrians_per_day)
        form_layout_general_information.addRow('Cyclist Volume per Day', input_general_info_road_cyclist_per_day)
        form_layout_general_information.addRow('Northbound / Eastbound', input_general_info_road_no_traffic_lanes_northbound_or_eastbound)
        form_layout_general_information.addRow('Southbound / Westbound', input_general_info_road_no_traffic_lanes_southbound_or_westbound)
        form_layout_general_information.addRow('Bidirectional', input_general_info_road_no_traffic_lanes_bidirectional)
        #TODO form_layout_general_information.addRow('Total', input_general_info_road_no_traffic_lanes_total)
        form_layout_general_information.addRow('Does Grade Crossing Include sidewalk, Path, or Trail?', input_general_info_road_sidewalks)
        form_layout_general_information.addRow('Regular Use of Crossing by Persons with Assistive Devices?', input_general_info_road_assistive_pedestrian_devices)
        form_layout_general_information.addRow('High Seasonal Fluctuation in Volumes?', input_general_info_road_seasonal_volume_fluctuations)
        form_layout_general_information.addRow('Is Crossing on a School Bus Route?', input_general_info_road_school_bus_route)
        form_layout_general_information.addRow('Do Dangerous Goods Trucks Use this Roadway?', input_general_info_road_dangerous_goods_route)
        form_layout_general_information.addRow('Other Special Road Users?', input_general_info_road_other_users)
        form_layout_general_information.addRow('Volume', input_general_info_road_other_users_daily_users)
        form_layout_general_information.addRow('Surrounding Land Use:', input_general_info_observe_surrounding_land_use)
        form_layout_general_information.addRow('Any schools, retirement homes, etc. nearby?', input_general_info_observe_special_buildings)
        form_layout_general_information.addRow('Urban/rural?', input_general_info_road_classification)
        form_layout_general_information.addRow('roadway Illumination?', input_general_info_observe_roadway_illumination)
        form_layout_general_information.addRow('Comments Regarding General Information', input_general_info_comments)

        # layout container widgets - DESIGN CONSIDERATIONS (GCS SECTION 10)
        form_layout_design_considerations.addRow('Design Vehicle Type:', input_design_road_design_vehicle_type)
        #TODO form_layout_design_considerations.addRow('Design Vehicle Class:', input_design_lookup_design_vehicle_class)
        #TODO form_layout_design_considerations.addRow('Design Vehicle Length (m):', input_design_lookup_design_vehicle_length)
        form_layout_design_considerations.addRow('Clearance Distance - Vehicle, cd (m):', input_design_measure_clearance_distance_vehicle)
        #TODO form_layout_design_considerations.addRow('Vehicle Travel Distance, S = L + cd (m):', input_design_calculate_vehicle_travel_distance)
        #TODO form_layout_design_considerations.addRow('Departure Time - Vehicle, Td = J + T:', input_design_calculate_clearance_time_crossing_vehicle_design_check)
        #TODO form_layout_design_considerations.addRow("Driver's Reaction Time (s):", input_design_input_reaction_time)
        form_layout_design_considerations.addRow('Maximum Road Approach Grade within S (%):', input_design_road_max_approach_grade_within_s)
        #TODO form_layout_design_considerations.addRow('Grade Adjustment Factor:', input_design_lookup_grade_adjustment_factor)
        form_layout_design_considerations.addRow('Do Field Acceleration Times Exceed Td?:', input_design_observe_field_acceleration_times_exceed_td)
        form_layout_design_considerations.addRow('Clearance Distance - Pedestrian, cd (m):', input_design_measure_clearance_distance_pedestrian)
        #TODO form_layout_design_considerations.addRow('Departure Time - Pedestrian, Td = J + T:', input_design_calculate_clearance_time_crossing_pedestrian_design_check)
        form_layout_design_considerations.addRow('Separation Distnace Between Adjacent Tracks (m):', input_design_measure_adjacent_track_separation_distance)      
        form_layout_design_considerations.addRow('Adjacent Track Clearance Distance (m):', input_design_measure_adjacent_track_clearance_distance)
        #TODO form_layout_design_considerations.addRow('Adjacent Track Clearance Time (s):', input_design_calculate_adjacent_track_clearance_time)
        #TODO form_layout_design_considerations.addRow('', input_design_calculate_clearance_time_gate_arm_ssd)
        #TODO form_layout_design_considerations.addRow('', input_design_calculate_clearance_time_gate_arm_stop)
        #TODO form_layout_design_considerations.addRow('', input_design_lookup_vehicle_departure_time_crossing)
        #TODO form_layout_design_considerations.addRow('', input_design_lookup_vehicle_departure_time_gate_arm_clearance)        
        #TODO form_layout_design_considerations.addRow('Design Consideration Comments', input_design_comments)

        # layout container widgets - LOCATION OF GRADE CROSSING (GCS SECTION 11)
        form_layout_location_of_crossing.addRow('D (intersection with stop sign) (N or E Road Approach) (m):', input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach)
        form_layout_location_of_crossing.addRow('D (intersection with stop sign) (S or W Road Approach) (m):', input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach)
        form_layout_location_of_crossing.addRow('D (signalized intersection) (N or E Road Approach) (m):', input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach)
        form_layout_location_of_crossing.addRow('D (signalized intersection) (S or W Road Approach) (m):', input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach)
        form_layout_location_of_crossing.addRow('D (other intersection/driveway/crosswalk) (N or E Road Approach) (m):', input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach)
        form_layout_location_of_crossing.addRow('D (other intersection/driveway/crosswalk) (S or W Road Approach) (m):', input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach)        
        form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles might queue onto the tracks?:', input_location_of_grade_crossing_queue_condition)
        form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles turning from a side street might not see warning devices for the crossing?:', input_location_of_grade_crossing_visibility_of_warning_lights)
        form_layout_location_of_crossing.addRow('Are there pedestrian crossings on either road approach that could cause vehicles to queue back to the tracks?:', input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk)
        form_layout_location_of_crossing.addRow('Location of Grade Crossing Comments:', input_location_of_grade_crossing_comments)

        # layout container widgets - GRADE CROSSING SURFACE (GCS SECTION 5)
        form_layout_crossing_surface.addRow('Is the crossing smooth enough to allow road vehicles, pedestrians, cyclists, and other road users to cross at their normal speed without consequence? Comments below.', input_grade_crossing_surface_observe_crossing_smoothness)
        form_layout_crossing_surface.addRow('Grade Crossing Surface Material', input_grade_crossing_surface_observe_material)
        form_layout_crossing_surface.addRow('Grade Crossing Surface Condition', input_grade_crossing_surface_observe_crossing_surface_condition)
        form_layout_crossing_surface.addRow('Road Approach Surface Type', input_grade_crossing_surface_observe_road_approach_surface_type)
        form_layout_crossing_surface.addRow('Road Approach Surface Condition', input_grade_crossing_surface_observe_road_approach_surface_condition)        
        form_layout_crossing_surface.addRow('Crossing Surface Width (m):', input_grade_crossing_surface_measure_crossing_surface_width)
        form_layout_crossing_surface.addRow('Centre Lane/Median Width (m):', input_grade_crossing_surface_measure_road_surface_median_width)
        form_layout_crossing_surface.addRow('Travelled Way Width (N or E Road Approach) (m):', input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach)
        form_layout_crossing_surface.addRow('Travelled Way Width (S or W Road Approach) (m):', input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach)
        form_layout_crossing_surface.addRow('Paved Shoulder Width (N or E Rail Approach) (m):', input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach)
        form_layout_crossing_surface.addRow('Paved Shoulder Width (S or W Rail Approach) (m):', input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach)
        form_layout_crossing_surface.addRow('Surface Extension beyond Travel Lanes/Shoulder (N or E Rail Approach) (m):', input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach)
        form_layout_crossing_surface.addRow('Surface Extension beyond Travel Lanes/Shoulder (S or W Rail Approach) (m):', input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach)
        form_layout_crossing_surface.addRow('Sidewalk/Path/Trail Width (N or E Rail Approach) (m):', input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach)
        form_layout_crossing_surface.addRow('Sidewalk/Path/Trail Width (S or W Rail Approach) (m):', input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach)
        form_layout_crossing_surface.addRow('Surface Extension beyond Sidewalk/Path/Trail (N or E Rail Approach) (m):', input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach)
        form_layout_crossing_surface.addRow('Surface Extension beyond Sidewalk/Path/Trail (S or W Rail Approach) (m):', input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach)
        form_layout_crossing_surface.addRow('Distance Between Travel Lane/Shoulder and Sidewalk/Path/Trail (N or E Rail Approach) (m):', input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach)
        form_layout_crossing_surface.addRow('Distance Between Travel Lane/Shoulder and Sidewalk/Path/Trail (S or W Rail Approach) (m):', input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach)
        form_layout_crossing_surface.addRow('', input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach)
        form_layout_crossing_surface.addRow('', input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach)
        form_layout_crossing_surface.addRow('Flangeway Depth (mm):', input_grade_crossing_surface_measure_flangeway_depth)
        form_layout_crossing_surface.addRow('Flangeway Width (mm):', input_grade_crossing_surface_measure_flangeway_width)
        form_layout_crossing_surface.addRow('Field Side Grinding Depth (mm):', input_grade_crossing_surface_measure_side_grinding_depth)
        form_layout_crossing_surface.addRow('Field Side Grinding Width (mm):', input_grade_crossing_surface_measure_side_grinding_width)
        form_layout_crossing_surface.addRow('Elevation of top of Rail Above Road Surface (mm):', input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface)
        form_layout_crossing_surface.addRow('Elevation of top of Rail Below Road Surface (mm):', input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface)
        form_layout_crossing_surface.addRow('Crossing Surface Comments:', input_grade_crossing_surface_comments)

        # layout container widgets - ROAD GEOMETRY (GCS SECTION 6)
        form_layout_road_geometry.addRow('', input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_road_general_approach_grade_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_road_general_approach_grade_s_or_w_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach)
        #form_layout_road_geometry.addRow('', input_road_geometry_lookup_gradient_difference)
        form_layout_road_geometry.addRow('', input_road_geometry_measure_railway_cross_slope)
        form_layout_road_geometry.addRow('', input_road_geometry_rail_superelevation_n_or_e_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_rail_superelevation_s_or_w_approach)
        form_layout_road_geometry.addRow('', input_road_geometry_observe_low_bed_truck_condition)
        form_layout_road_geometry.addRow('', input_road_geometry_road_crossing_angle)
        form_layout_road_geometry.addRow('', input_road_geometry_comments)

        # layout container widgets - SIGHTLINES (GCS SECTION 7)
        #TODO form_layout_sightlines.addRow('', input_sightlines_calculate_Dssd_vehicle_Min_ft)
        #TODO form_layout_sightlines.addRow('', input_sightlines_calculate_Dssd_vehicle_Min_m)
        #TODO form_layout_sightlines.addRow('', input_sightlines_calculate_Dstopped_pedestrian_Min_ft)
        #TODO form_layout_sightlines.addRow('', input_sightlines_calculate_Dstopped_pedestrian_Min_m)
        #TODO form_layout_sightlines.addRow('', input_sightlines_calculate_Dstopped_vehicle_Min_ft)
        #TODO form_layout_sightlines.addRow('', input_sightlines_calculate_Dstopped_vehicle_Min_m)
        form_layout_sightlines.addRow('', input_sightlines_comments)
        #TODO form_layout_sightlines.addRow('', input_sightlines_lookup_ssd_minimum_n_or_e_approach)
        #TODO form_layout_sightlines.addRow('', input_sightlines_lookup_ssd_minimum_s_or_w_approach)
        form_layout_sightlines.addRow('', input_sightlines_measure_dssd_actual_n_or_e_approach_left)
        form_layout_sightlines.addRow('', input_sightlines_measure_dssd_actual_n_or_e_approach_right)
        form_layout_sightlines.addRow('', input_sightlines_measure_dssd_actual_s_or_w_approach_left)
        form_layout_sightlines.addRow('', input_sightlines_measure_dssd_actual_s_or_w_approach_right)
        form_layout_sightlines.addRow('', input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left)
        form_layout_sightlines.addRow('', input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right)
        form_layout_sightlines.addRow('', input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left)
        form_layout_sightlines.addRow('', input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right)
        form_layout_sightlines.addRow('', input_sightlines_measure_ssd_actual_n_or_e_approach)
        form_layout_sightlines.addRow('', input_sightlines_measure_ssd_actual_s_or_w_approach)
        form_layout_sightlines.addRow('', input_sightlines_observe_sightline_obstructions)

        # layout container widgets - SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_advisory_speed_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_advisory_speed_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_advisory_speed_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_dividing_lines_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_comments
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_n_or_e_approach_condition)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_n_or_e_approach_legible)
        #TODO form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_n_or_e_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_s_or_w_approach_condition)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_s_or_w_approach_legible)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_s_or_w_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_emergency_notification_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_number_of_tracks_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_per_mutcd)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_posted_speed_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_posted_speed_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_railway_crossing_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_sidewalks_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_n_or_e_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_n_or_e_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_n_or_e_approach_same_post)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_s_or_w_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_s_or_w_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_s_or_w_approach_same_post)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_comments)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present)

        # layout container widgets - GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_private_9_3_1)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_private_9_3_2_a)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_private_9_3_2_b)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_private_9_3_2_c)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_public_9_1_a)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_public_9_1_b)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_public_9_1_c)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_public_9_1_d_i)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_public_9_1_d_ii)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_public_9_1_d_iii)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrant_sidewalk_9_5)
        #TODO form_layout_gcws_warrants.addRow('', input_gcws_warrants_comments)

        # layout container widgets - GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_n_or_e_approach_distance_from_road)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_s_or_w_approach_distance_from_road)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation)
        form_layout_gcws.addRow('', input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation)
        form_layout_gcws.addRow('', input_gcws_observe_bell_if_sidewalk)
        form_layout_gcws.addRow('', input_gcws_observe_bells_condition)
        form_layout_gcws.addRow('', input_gcws_observe_bells_n_or_e_approach)
        form_layout_gcws.addRow('', input_gcws_observe_bells_s_or_w_approach)
        form_layout_gcws.addRow('', input_gcws_observe_cantilever_lights_condition)
        form_layout_gcws.addRow('', input_gcws_observe_cantilever_lights_n_or_e_approach)
        form_layout_gcws.addRow('', input_gcws_observe_cantilever_lights_s_or_w_approach)
        form_layout_gcws.addRow('', input_gcws_observe_gates_condition)
        form_layout_gcws.addRow('', input_gcws_observe_gates_n_or_e_approach)
        form_layout_gcws.addRow('', input_gcws_observe_gates_s_or_w_approach)
        form_layout_gcws.addRow('', input_gcws_observe_gcws_limited_use_with_walk_light_assembly)
        form_layout_gcws.addRow('', input_gcws_observe_gcws_limited_use_without_walk_light_assembly)
        form_layout_gcws.addRow('', input_gcws_observe_light_units_condition)
        form_layout_gcws.addRow('', input_gcws_observe_light_units_n_or_e_approach)
        form_layout_gcws.addRow('', input_gcws_observe_light_units_s_or_w_approach)
        form_layout_gcws.addRow('', input_gcws_observe_warning_time_consistency)
        form_layout_gcws.addRow('', input_gcws_observe_warning_time_consistency_reduced_speed)
        form_layout_gcws.addRow('', input_gcws_rail_crossing_warning_time_actual)
        form_layout_gcws.addRow('', input_gcws_rail_cut_out_circuit_requirements)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_approach_warning_time)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_adjacent_crossing)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_clearance_distance)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_departure_time_pedestrian)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_departure_time_vehicle)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_gate_arm_clearance)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_preemption)
        #TODO form_layout_gcws.addRow('', input_gcws_rail_design_warning_time_ssd)
        form_layout_gcws.addRow('', input_gcws_rail_directional_stick_circuit_requirements)
        form_layout_gcws.addRow('', input_gcws_rail_self_diagnostic)

        # layout container widgets - FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        form_layout_gcws_lights.addRow('', input_light_units_comments)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_n_or_e_approach_dl)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_n_or_e_approach_dr)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_n_or_e_approach_height)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_s_or_w_approach_dl)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_s_or_w_approach_dr)
        form_layout_gcws_lights.addRow('', input_light_units_measure_cantilevers_s_or_w_approach_height)
        form_layout_gcws_lights.addRow('', input_light_units_measure_n_or_e_approach_height)
        form_layout_gcws_lights.addRow('', input_light_units_measure_s_or_w_approach_height)
        form_layout_gcws_lights.addRow('', input_light_units_observe_cantilevers_n_or_e_approach_per_fig_12_3)
        form_layout_gcws_lights.addRow('', input_light_units_observe_n_or_e_approach_per_fig_12_1)
        form_layout_gcws_lights.addRow('', input_light_units_observe_sidewalks_n_or_e_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_sidewalks_s_or_w_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_supplemental_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_supplemental_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_visibility_back_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_visibility_back_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_visibility_front_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('', input_light_units_observe_visibility_front_lights_s_or_w_approach)

        # layout container widgets - GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_calculate_gate_arm_clearance_time_recommended)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        form_layout_gcws_gates.addRow('', input_gates_gcws_comments)
        form_layout_gcws_gates.addRow('', input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach)
        form_layout_gcws_gates.addRow('', input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach)
        form_layout_gcws_gates.addRow('', input_gates_gcws_measure_gate_ascent_time)
        form_layout_gcws_gates.addRow('', input_gates_gcws_measure_gate_descent_time)
        form_layout_gcws_gates.addRow('', input_gates_gcws_observe_gate_arm_rest)
        form_layout_gcws_gates.addRow('', input_gates_gcws_observe_gate_ascent_time)
        form_layout_gcws_gates.addRow('', input_gates_gcws_observe_gate_descent_time)
        form_layout_gcws_gates.addRow('', input_gates_gcws_observe_gate_strips_n_or_e_approach)
        form_layout_gcws_gates.addRow('', input_gates_gcws_observe_gate_strips_s_or_w_approach)
        form_layout_gcws_gates.addRow('', input_gates_gcws_observe_per_fig_12_2)
        form_layout_gcws_gates.addRow('', input_gates_gcws_rail_gate_arm_delay_time_design)
        form_layout_gcws_gates.addRow('', input_gates_gcws_rail_gate_arm_descent_time_design)
        form_layout_gcws_gates.addRow('', input_gates_gcws_rail_inner_gate_arm_delay_time_design)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_private_9_4_1_a)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_private_9_4_1_b)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_private_9_4_1_c)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_public_9_2_1_a)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_public_9_2_1_b)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_public_9_2_1_c)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_public_9_2_1_d)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_public_9_2_1_e)
        #TODO form_layout_gcws_gates.addRow('', input_gates_gcws_warrant_sidewalk_9_6)

        # layout container widgets - PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #TODO form_layout_aaws.addRow('', input_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        #TODO form_layout_aaws.addRow('', input_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        #TODO form_layout_aaws.addRow('', input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        #TODO form_layout_aaws.addRow('', input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        form_layout_aaws.addRow('', input_aawd_comments)
        form_layout_aaws.addRow('', input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual)
        form_layout_aaws.addRow('', input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual)
        form_layout_aaws.addRow('', input_aawd_observe_present_n_or_e_approach)
        form_layout_aaws.addRow('', input_aawd_observe_present_s_or_w_approach)
        form_layout_aaws.addRow('', input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach)
        form_layout_aaws.addRow('', input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach)
        #TODO form_layout_aaws.addRow('', input_aawd_warrant_gcr_lookup_road_classification)
        #TODO form_layout_aaws.addRow('', input_aawd_warrant_gcr_observe_environmental_condition)
        #TODO form_layout_aaws.addRow('', input_aawd_warrant_gcr_observe_sightline_Obstruction)
        #TODO form_layout_aaws.addRow('', input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        #TODO form_layout_aaws.addRow('', input_aawd_warrant_mutcd_lookup_significant_road_downgrade)

        # layout container widgets - INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #TODO form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_lookup_proximity_condition)
        #TODO form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_lookup_required)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_known_queuing_issues)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_pedestrian_accommodation)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_queuing_condition)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_supplemental_signage)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals_comments)
        #TODO form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_road_date_Last_preemption_check)
        #TODO form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_road_preemption_warning_time_actual)
        form_layout_interconnection_traffic_signals.addRow('', input_preemption_of_traffic_signals_road_preemption_warning_time_design)

        # layout container widgets - WHISTLE CESSATION (GCS SECTION Appendix D)
        form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_comments)
        #TODO form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_lookup_gcs_12_to_16)
        #TODO form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_lookup_gcs_9_2)
        #TODO form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_observe_For_stop_and_proceed)
        form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_observe_trespassing_area)
        form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_rail_anti_whistling_zone)
        form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_rail_anti_whistling_zone_24_Hrs)
        #TODO form_layout_whistle_cessation.addRow('', input_areas_without_train_whistling_requirements_observe_table_D1)
        '''

        #######################
        # Size Control Layout #
        #######################

        # use stretch factor

        stretch_layout = qtw.QHBoxLayout()
        main_layout.addLayout(stretch_layout)
        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)
        
        #############################
        # Container Widgets         #
        #############################

        # QTabWidget
        tab_widget = qtw.QTabWidget(
            movable=True,
            tabPosition=qtw.QTabWidget.North,
            tabShape=qtw.QTabWidget.Triangular
        )
        main_layout.addWidget(tab_widget)
        tab_widget.addTab(container_inspection_details, 'INSPECTION DETAILS')
        tab_widget.addTab(container_collision_history, 'COLLISION HISTORY (5 YEAR PERIOD)')
        tab_widget.addTab(container_general_information, 'GENERAL INFORMATION')
        tab_widget.addTab(container_design_considerations, 'DESIGN CONSIDERATIONS (GCS SECTION 10)')
        tab_widget.addTab(container_location_of_crossing, 'LOCATION OF GRADE CROSSING (GCS SECTION 11)')
        tab_widget.addTab(container_crossing_surface, 'CROSSING SURFACE (GCS SECTION 5)')
        tab_widget.addTab(container_road_geometry, 'ROAD GEOMETRY (GCS SECTION 6)')
        tab_widget.addTab(container_sightlines, 'SIGHTLINES (GCS SECTION 7)')
        tab_widget.addTab(container_signs_and_pavement_markings, 'SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)')
        tab_widget.addTab(container_gcws_warrants, 'GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)')
        tab_widget.addTab(container_gcws, 'GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)')
        tab_widget.addTab(container_gcws_lights, 'FLASHING LIGHT UNITS (GCS SECTION 13 & 14)')
        tab_widget.addTab(container_gcws_gates, 'GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)')
        tab_widget.addTab(container_aaws, 'PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)')
        tab_widget.addTab(container_interconnection_traffic_signals, 'INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)')
        tab_widget.addTab(container_whistle_cessation, 'WHISTLE CESSATION (GCS SECTION Appendix D)')
        tab_widget.setMovable(True)

        '''
        ######################
        # The central widget #
        ######################
        self.textedit = qtw.QTextEdit()
        self.setCentralWidget(self.textedit)

        #################
        # The Statusbar #
        #################

        # The long way 'round
        #status_bar = qtw.QStatusBar()
        #self.setStatusBar(status_bar)
        #status_bar.showMessage('Welcome to text_editor.py')

        # The short way 'round
        self.statusBar().showMessage('Welcome to text_editor.py')

        # add widgets to statusbar
        charcount_label = qtw.QLabel("chars: 0")
        self.textedit.textChanged.connect(
            lambda: charcount_label.setText(
                "chars: " +
                str(len(self.textedit.toPlainText()))
                )
            )
        self.statusBar().addPermanentWidget(charcount_label)

        ###############j
        # The menubar #
        ###############
        menubar = self.menuBar()

        # add submenus to a menu
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        help_menu = menubar.addMenu('Help')

        # add actions
        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')

        # add separator
        file_menu.addSeparator()

        # add an action with a callback
        # Errata:  The book contains this line:
        #quit_action = file_menu.addAction('Quit', self.destroy)
        # It should call self.close instead, like so:
        quit_action = file_menu.addAction('Quit', self.close)

        # connect to a Qt Slot
        edit_menu.addAction('Undo', self.textedit.undo)

        # create a QAction manually

        redo_action = qtw.QAction('Redo', self)
        redo_action.triggered.connect(self.textedit.redo)
        edit_menu.addAction(redo_action)

        ############################
        # The Toolbar and QActions #
        ############################

        toolbar = self.addToolBar('File')
        #toolbar.addAction(open_action)
        #toolbar.addAction("Save")

        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setAllowedareas(
            qtc.Qt.topToolBararea |
            qtc.Qt.BottomToolBararea
        )

        # Add with icons
        open_icon = self.style().standardIcon(qtw.QStyle.SP_DirOpenIcon)
        save_icon = self.style().standardIcon(qtw.QStyle.SP_DriveHDIcon)

        open_action.setIcon(open_icon)
        toolbar.addAction(open_action)
        toolbar.addAction(
            save_icon,
            'Save',
            lambda: self.statusBar().showMessage('File Saved!')
        )

        # create a custom QAction

        help_action = qtw.QAction(
            self.style().standardIcon(qtw.QStyle.SP_DialogHelpButton),
            'Help',
            self,  # important to pass the parent!
            triggered=lambda: self.statusBar().showMessage(
                'Sorry, no help yet!'
            )
        )
        toolbar.addAction(help_action)

        # create a toolbar in another part of the screen:
        toolbar2 = qtw.QToolBar('Edit')
        self.addToolBar(qtc.Qt.RightToolBararea, toolbar2)
        toolbar2.addAction('Copy', self.textedit.copy)
        toolbar2.addAction('Cut', self.textedit.cut)
        toolbar2.addAction('Paste', self.textedit.paste)


        ################
        # Dock Widgets #
        ################

        dock = qtw.QDockWidget("Replace")
        self.addDockWidget(qtc.Qt.LeftDockWidgetarea, dock)

        # make it not closable
        dock.setFeatures(
            qtw.QDockWidget.DockWidgetMovable |
            qtw.QDockWidget.DockWidgetFloatable
        )

        replace_widget = qtw.QWidget()
        replace_widget.setLayout(qtw.QVBoxLayout())
        dock.setWidget(replace_widget)

        self.search_text_inp = qtw.QLineEdit(placeholderText='search')
        self.replace_text_inp = qtw.QLineEdit(placeholderText='replace')
        search_and_replace_btn = qtw.QPushButton(
            "Search and Replace",
            clicked=self.search_and_replace
            )
        replace_widget.layout().addRow(input_self.search_text_inp)
        replace_widget.layout().addRow(input_self.replace_text_inp)
        replace_widget.layout().addRow(input_search_and_replace_btn)
        replace_widget.layout().addStretch()

        ############################
        # Messageboxes and Dialogs #
        ############################

        # QMessageBox
        help_menu.addAction('About', self.showAboutDialog)

        if self.settings.value('show_warnings', False, type=bool):
            response = qtw.QMessageBox.question(
                self,
                'My Text Editor',
                'This is beta software, do you want to continue?',
                qtw.QMessageBox.Yes | qtw.QMessageBox.Abort
            )
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

            # custom message box

            splash_screen = qtw.QMessageBox()
            splash_screen.setWindowTitle('My Text Editor')
            splash_screen.setText('BETA SOFTWARE WARNING!')
            splash_screen.setInformativeText(
                'This is very, very beta, '
                'are you really sure you want to use it?'
            )
            splash_screen.setDetailedText(
                'This editor was written for pedagogical '
                'purposes, and probably is not fit for real work.'
            )
            splash_screen.setWindowModality(qtc.Qt.WindowModal)
            splash_screen.addButton(qtw.QMessageBox.Yes)
            splash_screen.addButton(qtw.QMessageBox.Abort)
            response = splash_screen.exec_()
            if response == qtw.QMessageBox.Abort:
                self.close()
                sys.exit()

        # QFileDialog
        open_action.triggered.connect(self.openFile)
        save_action.triggered.connect(self.saveFile)

        # QFontDialog

        edit_menu.addAction('Set Font…', self.set_font)

        # Custom dialog
        edit_menu.addAction('Settings…', self.show_settings)

        ###################
        # Saving Settings #
        ###################


        # end main UI code
        self.show()

    def search_and_replace(self):
        s_text = self.search_text_inp.text()
        r_text = self.replace_text_inp.text()

        if s_text:
            self.textedit.setText(
                self.textedit.toPlainText().replace(s_text, r_text)
                )

    def showAboutDialog(self):
        qtw.QMessageBox.about(
            self,
            "About text_editor.py",
            "This is a text editor written in PyQt5."
        )

    def openFile(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)',
            'Python Files (*.py)',
            qtw.QFileDialog.DontUseNativeDialog |
            qtw.QFileDialog.DontResolveSymlinks
        )
        if filename:
            try:
                with open(filename, 'r') as fh:
                    self.textedit.setText(fh.read())
            except Exception as e:
                # Errata:  Book contains the following line:
                #qtw.QMessageBox.critical(f"Could not load file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def saveFile(self):
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "Select the file to save to…",
            qtc.QDir.homePath(),
            'Text Files (*.txt) ;;Python Files (*.py) ;;All Files (*)'
        )
        if filename:
            try:
                with open(filename, 'w') as fh:
                    fh.write(self.textedit.toPlainText())
            except Exception as e:
                # Errata:  Book contains this line:
                #qtw.QMessageBox.critical(f"Could not save file: {e}")
                # It should read like this:
                qtw.QMessageBox.critical(self, f"Could not load file: {e}")

    def set_font(self):
        current = self.textedit.currentFont()
        font, accepted = qtw.QFontDialog.getFont(
            current,
            self,
            options=(
                qtw.QFontDialog.DontUseNativeDialog |
                qtw.QFontDialog.MonospacedFonts
            )
        )
        if accepted:
            self.textedit.setCurrentFont(font)

    def show_settings(self):

        settings_dialog = SettingsDialog(self.settings, self)
        settings_dialog.exec()
        '''