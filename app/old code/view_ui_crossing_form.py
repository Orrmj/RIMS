from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class UI_CrossingForm(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Crossing Assessment Form')
        self.formWidgets()
        self.show()
    
    def formWidgets(self):    
        """
        Create widgets that will be used in the application self.form. 
        """

        # Combo Box Lists
        list_yes_no = ['', 'Yes', 'No']
        list_yes_no_na = ['', 'Yes', 'No', 'N/A']
        list_condition = ['', 'Good', 'Fair', 'Poor']
        list_inspection_details_gcws_type = ['','Active','Passive']
        list_inspection_details_grade_crossing_type = ['','Public', 'Private (CTA 102-Type)', 'Private (CTA 103-Type)']
        list_inspection_details_track_type = ['','Mainline', 'Industrial Spur', 'Mainline Spur', 'Yard, Other']
        list_inspection_details_province = ['', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'ON', 'QC', 'SK', 'YT']
        list_inspection_details_reason_for_assessment = [
            "",
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
        list_general_info_road_classification = ['', 'Rural Local Undivided', 'Rural Collector Undivided',
            'Rural Collector Divided', 'Rural Arterial Undivided', 'Rural Arterial Divided', 'Rural Freeway Divided',
            'Urban Local Undivided', 'Urban Collector Undivided', 'Urban Collector Divided', 'Urban Arterial Undivided',
            'Urban Arterial Divided', 'Private Road', 'Pedestrian Crossing']
        list_general_info_observe_surrounding_land_use = ['', 'Farm', 'Residential', 'Recreational', 'Industrial', 'Commercial']
        list_design_road_design_vehicle_type = ['Passenger Cars, Vans, and Pickups', 'Light Single-Unit Trucks',
            'Medium Single-Unit Trucks', 'Heavy Single-Unit Trucks', 'WB-19 Tractor-Semitrailers', 
            'WB-20 Tractor-Semitrailers', 'A-Train Doubles (ATD)', 'B-Train Doubles', 'Standard Single-Unit Buses (B-12)',
            'Articulated Buses (A-Bus)', 'Intercity Buses (I-Bus)', 'Pedestrian Only']
        list_grade_crossing_surface_observe_material = ['', 'Timber', 'Asphalt', 'Asphalt and Flange', 
            'Concrete', 'Concrete and Rubber', 'Rubber', 'Metal', 'Unconsolidated', 'Other']
        list_grade_crossing_surface_observe_road_approach_surface_type = ['', 'Asphalt', 'Concrete', 'Gravel']
        list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = ['', 'Not Interconnected', 'Advance Preemption', 'Simultaneous Preemption']
                
        # INSPECTION DETAILS
        #Group TextBoxes
        self.input_inspection_details_assessment_team = qtw.QTextEdit()
        
        '''
        #Group DatePicker
        self.input_inspection_details_date_assessment = qtw.QDatetimeEdit(
            self,
            date=datetime.date.today(),
            calendarPopup=True,
            displayFormat='yyyy-MM-dd'
        )
        '''

        #Group LineEdits
        self.input_inspection_details_crossing_location = qtw.QLineEdit() 
        self.input_inspection_details_latitude = qtw.QLineEdit() 
        self.input_inspection_details_location_number = qtw.QLineEdit() 
        self.input_inspection_details_longitude = qtw.QLineEdit() 
        self.input_inspection_details_municipality = qtw.QLineEdit() 
        self.input_inspection_details_road_name = qtw.QLineEdit() 
        self.input_inspection_details_road_number = qtw.QLineEdit() 
        self.input_inspection_details_spur_mile = qtw.QLineEdit() 
        self.input_inspection_details_spur_name = qtw.QLineEdit() 
        self.input_inspection_details_subdivision_mile = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_inspection_details_gcws_type = qtw.QComboBox()
        self.input_inspection_details_gcws_type.addItems(list_inspection_details_gcws_type)

        self.input_inspection_details_grade_crossing_type = qtw.QComboBox()
        self.input_inspection_details_grade_crossing_type.addItems(list_inspection_details_grade_crossing_type)

        self.input_inspection_details_province = qtw.QComboBox()
        self.input_inspection_details_province.addItems(list_inspection_details_province)

        self.input_inspection_details_railway_authority = qtw.QComboBox()
        #TODO create and add railway authority list 

        self.input_inspection_details_reason_for_assessment = qtw.QComboBox()
        self.input_inspection_details_reason_for_assessment.addItems(list_inspection_details_reason_for_assessment)
        
        self.input_inspection_details_road_authority = qtw.QComboBox()
        #TODO create and add road authority list 

        self.input_inspection_details_subdivision_name = qtw.QComboBox()
        #TODO create and add subdivision list 

        self.input_inspection_details_track_type = qtw.QComboBox()
        self.input_inspection_details_track_type.addItems(list_inspection_details_track_type)

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        self.input_collision_history_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_collision_history_fatal_injury = qtw.QLineEdit() 
        self.input_collision_history_fatalities = qtw.QLineEdit() 
        self.input_collision_history_personal_injuries = qtw.QLineEdit() 
        self.input_collision_history_personal_injury = qtw.QLineEdit() 
        self.input_collision_history_property_damage = qtw.QLineEdit()

        #Group Labels 
        #TODO self.input_collision_history_total_5_year_period = pass

        # GENERAL INFORMATION
        #Group TextEdits
        self.input_general_info_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_general_info_observe_special_buildings = qtw.QLineEdit() 
        self.input_general_info_rail_max_railway_operating_speed_freight = qtw.QLineEdit() 
        self.input_general_info_rail_max_railway_operating_speed_passenger = qtw.QLineEdit() 
        self.input_general_info_rail_no_trains_per_day_freight = qtw.QLineEdit() 
        self.input_general_info_rail_no_trains_per_day_passengers = qtw.QLineEdit() 
        self.input_general_info_rail_railway_design_speed = qtw.QLineEdit() 
        self.input_general_info_road_aadt_current = qtw.QLineEdit() 
        self.input_general_info_road_aadt_forecast = qtw.QLineEdit() 
        self.input_general_info_road_aadt_year_current = qtw.QLineEdit() 
        self.input_general_info_road_aadt_year_forecasted = qtw.QLineEdit() 
        self.input_general_info_road_cyclist_per_day = qtw.QLineEdit() 
        self.input_general_info_road_no_traffic_lanes_bidirectional = qtw.QLineEdit() 
        self.input_general_info_road_no_traffic_lanes_northbound_or_eastbound = qtw.QLineEdit() 
        self.input_general_info_road_no_traffic_lanes_southbound_or_westbound = qtw.QLineEdit() 
        self.input_general_info_road_other_users = qtw.QLineEdit() 
        self.input_general_info_road_other_users_daily_users = qtw.QLineEdit() 
        self.input_general_info_road_pedestrians_per_day = qtw.QLineEdit() 
        self.input_general_info_road_speed_design = qtw.QLineEdit() 
        self.input_general_info_road_speed_posted = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_general_info_observe_roadway_illumination = qtw.QComboBox()
        self.input_general_info_observe_roadway_illumination.addItems(list_yes_no)

        self.input_general_info_observe_surrounding_land_use = qtw.QComboBox()
        self.input_general_info_observe_surrounding_land_use.addItems(list_general_info_observe_surrounding_land_use)

        self.input_general_info_rail_train_switching = qtw.QComboBox()
        self.input_general_info_rail_train_switching.addItems(list_yes_no)
        
        self.input_general_info_road_assistive_pedestrian_devices = qtw.QComboBox()
        self.input_general_info_road_assistive_pedestrian_devices.addItems(list_yes_no)

        self.input_general_info_road_classification = qtw.QComboBox()
        self.input_general_info_road_classification.addItems(list_general_info_road_classification)
        
        self.input_general_info_road_dangerous_goods_route = qtw.QComboBox()
        self.input_general_info_road_dangerous_goods_route.addItems(list_yes_no)

        self.input_general_info_road_school_bus_route = qtw.QComboBox()
        self.input_general_info_road_school_bus_route.addItems(list_yes_no)


        self.input_general_info_road_seasonal_volume_fluctuations = qtw.QComboBox()
        self.input_general_info_road_seasonal_volume_fluctuations.addItems(list_yes_no)

        self.input_general_info_road_sidewalks = qtw.QComboBox()
        self.input_general_info_road_sidewalks.addItems(list_yes_no)

        #Group Labels
        #TODO self.input_general_info_rail_no_tracks_total = pass
        #TODO self.input_general_info_rail_no_trains_per_day_total = pass
        #TODO self.input_general_info_road_no_traffic_lanes_total = pass

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        self.input_design_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_design_measure_adjacent_track_clearance_distance = qtw.QLineEdit() 
        self.input_design_measure_adjacent_track_separation_distance = qtw.QLineEdit() 
        self.input_design_measure_clearance_distance_pedestrian = qtw.QLineEdit() 
        self.input_design_measure_clearance_distance_vehicle = qtw.QLineEdit() 
        self.input_design_road_max_approach_grade_within_s = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_design_observe_field_acceleration_times_exceed_td = qtw.QComboBox()
        self.input_design_observe_field_acceleration_times_exceed_td.addItems(list_yes_no)

        self.input_design_road_design_vehicle_type = qtw.QComboBox()
        self.input_design_road_design_vehicle_type.addItems(list_design_road_design_vehicle_type)

        #Group Labels
        #TODO self.input_design_calculate_adjacent_track_clearance_time = pass
        #TODO self.input_design_calculate_clearance_time_crossing_pedestrian_design_check = pass
        #TODO self.input_design_calculate_clearance_time_crossing_vehicle_design_check = pass
        #TODO self.input_design_calculate_clearance_time_gate_arm_ssd = pass
        #TODO self.input_design_calculate_clearance_time_gate_arm_stop = pass
        #TODO self.input_design_calculate_vehicle_travel_distance = pass
        #TODO self.input_design_self.input_reaction_time = pass
        #TODO self.input_design_lookup_design_vehicle_class = pass
        #TODO self.input_design_lookup_design_vehicle_length = pass
        #TODO self.input_design_lookup_grade_adjustment_factor = pass
        #TODO self.input_design_lookup_vehicle_departure_time_crossing = pass
        #TODO self.input_design_lookup_vehicle_departure_time_gate_arm_clearance = pass
        
        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        self.input_location_of_grade_crossing_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = qtw.QLineEdit() 
        self.input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = qtw.QLineEdit() 
        self.input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = qtw.QLineEdit() 
        self.input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = qtw.QLineEdit() 
        self.input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = qtw.QLineEdit() 
        self.input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = qtw.QLineEdit() 

        #group ComboBoxes
        self.input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = qtw.QComboBox()
        self.input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk.addItems(list_yes_no)

        self.input_location_of_grade_crossing_queue_condition = qtw.QComboBox()
        self.input_location_of_grade_crossing_queue_condition.addItems(list_yes_no)

        self.input_location_of_grade_crossing_visibility_of_warning_lights = qtw.QComboBox()
        self.input_location_of_grade_crossing_queue_condition.addItems(list_yes_no)
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        self.input_grade_crossing_surface_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_crossing_surface_width = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_flangeway_depth = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_flangeway_width = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_road_surface_median_width = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_side_grinding_depth = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_side_grinding_width = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = qtw.QLineEdit() 
        self.input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_grade_crossing_surface_observe_crossing_smoothness = qtw.QComboBox()
        self.input_grade_crossing_surface_observe_crossing_smoothness.addItems(list_yes_no)

        self.input_grade_crossing_surface_observe_crossing_surface_condition = qtw.QComboBox()
        self.input_grade_crossing_surface_observe_crossing_smoothness.addItems(list_condition)

        self.input_grade_crossing_surface_observe_material = qtw.QComboBox()
        self.input_grade_crossing_surface_observe_material.addItems(list_grade_crossing_surface_observe_material)

        self.input_grade_crossing_surface_observe_road_approach_surface_condition = qtw.QComboBox()
        self.input_grade_crossing_surface_observe_road_approach_surface_condition.addItems(list_condition)

        self.input_grade_crossing_surface_observe_road_approach_surface_type = qtw.QComboBox()
        self.input_grade_crossing_surface_observe_road_approach_surface_type.addItems(list_grade_crossing_surface_observe_road_approach_surface_type)

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        self.input_road_geometry_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_road_geometry_measure_railway_cross_slope = qtw.QLineEdit() 
        self.input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = qtw.QLineEdit() 
        self.input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = qtw.QLineEdit() 
        self.input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = qtw.QLineEdit() 
        self.input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = qtw.QLineEdit() 
        self.input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = qtw.QLineEdit() 
        self.input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = qtw.QLineEdit() 
        self.input_road_geometry_rail_superelevation_n_or_e_approach = qtw.QLineEdit() 
        self.input_road_geometry_rail_superelevation_s_or_w_approach = qtw.QLineEdit() 
        self.input_road_geometry_road_crossing_angle = qtw.QLineEdit() 
        self.input_road_geometry_road_general_approach_grade_n_or_e_approach = qtw.QLineEdit() 
        self.input_road_geometry_road_general_approach_grade_s_or_w_approach = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = qtw.QComboBox()
        self.input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach.addItems(list_yes_no)

        self.input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = qtw.QComboBox()
        self.input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach.addItems(list_yes_no)

        self.input_road_geometry_observe_low_bed_truck_condition = qtw.QComboBox()
        self.input_road_geometry_observe_low_bed_truck_condition.addItems(list_yes_no)

        self.input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = qtw.QComboBox()
        self.input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach.addItems(list_yes_no)

        self.input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = qtw.QComboBox()
        self.input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach.addItems(list_yes_no)
       
        #Group Labels
        #TODO self.input_road_geometry_lookup_gradient_difference = pass
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        self.input_sightlines_comments = qtw.QTextEdit()
        
        #Group LineEdits
        self.input_sightlines_measure_dssd_actual_n_or_e_approach_left = qtw.QLineEdit() 
        self.input_sightlines_measure_dssd_actual_n_or_e_approach_right = qtw.QLineEdit() 
        self.input_sightlines_measure_dssd_actual_s_or_w_approach_left = qtw.QLineEdit() 
        self.input_sightlines_measure_dssd_actual_s_or_w_approach_right = qtw.QLineEdit() 
        self.input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = qtw.QLineEdit() 
        self.input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = qtw.QLineEdit() 
        self.input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = qtw.QLineEdit() 
        self.input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = qtw.QLineEdit() 
        self.input_sightlines_measure_ssd_actual_n_or_e_approach = qtw.QLineEdit() 
        self.input_sightlines_measure_ssd_actual_s_or_w_approach = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_sightlines_observe_sightline_obstructions = qtw.QComboBox()
        self.input_sightlines_observe_sightline_obstructions.addItems(list_yes_no)

        #Group Labels
        #TODO self.input_sightlines_calculate_dssd_vehicle_min_ft = pass
        #TODO self.input_sightlines_calculate_dssd_vehicle_min_m = pass
        #TODO self.input_sightlines_calculate_dstopped_pedestrian_min_ft = pass
        #TODO self.input_sightlines_calculate_dstopped_pedestrian_min_m = pass
        #TODO self.input_sightlines_calculate_dstopped_vehicle_min_ft = pass
        #TODO self.input_sightlines_calculate_dstopped_vehicle_min_m = pass
        #TODO self.input_sightlines_lookup_ssd_minimum_n_or_e_approach = pass
        #TODO self.input_sightlines_lookup_ssd_minimum_s_or_w_approach = pass

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE self.input_signs_and_markings_advisory_speed_comments = pass
        #DELETE self.input_signs_and_markings_comments = pass
        #DELETE self.input_signs_and_markings_emergency_notification_comments = pass
        #DELETE self.input_signs_and_markings_number_of_tracks_comments = pass
        #DELETE self.input_signs_and_markings_railway_crossing_ahead_comments = pass
        #DELETE self.input_signs_and_markings_railway_crossing_comments = pass
        #DELETE self.input_signs_and_markings_stop_comments = pass
        #DELETE self.input_signs_and_markings_stop_sign_ahead_comments = pass

        #Group LineEdits
        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = qtw.QLineEdit() 
        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = qtw.QLineEdit() 
        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = qtw.QLineEdit() 
        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = qtw.QLineEdit() 
        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = qtw.QLineEdit() 
        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_n_or_e_approach_height = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_n_or_e_approach_location_from_rail = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_n_or_e_approach_location_from_road = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_s_or_w_approach_height = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_s_or_w_approach_location_from_rail = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_s_or_w_approach_location_from_road = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = qtw.QLineEdit() 
        self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_signs_and_markings_advisory_speed_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_advisory_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = qtw.QComboBox()
        self.input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.input_signs_and_markings_advisory_speed_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_advisory_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = qtw.QComboBox()
        self.input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.input_signs_and_markings_dividing_lines_present = qtw.QComboBox()
        self.input_signs_and_markings_dividing_lines_present.addItems(list_yes_no)

        self.input_signs_and_markings_emergency_notification_n_or_e_approach_condition = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_n_or_e_approach_condition.addItems(list_condition)

        self.input_signs_and_markings_emergency_notification_n_or_e_approach_legible = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_n_or_e_approach_legible.addItems(list_yes_no_na)

        self.input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation = qtw.QComboBox()
        self.input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.input_signs_and_markings_emergency_notification_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_emergency_notification_s_or_w_approach_condition = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_s_or_w_approach_condition.addItems(list_condition)

        self.input_signs_and_markings_emergency_notification_s_or_w_approach_legible = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_s_or_w_approach_legible.addItems(list_yes_no_na)

        self.input_signs_and_markings_emergency_notification_s_or_w_approach_orientation = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.input_signs_and_markings_emergency_notification_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_emergency_notification_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = qtw.QComboBox()
        self.input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = qtw.QComboBox()
        self.input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.input_signs_and_markings_number_of_tracks_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_number_of_tracks_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = qtw.QComboBox()
        self.input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = qtw.QComboBox()
        self.input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.input_signs_and_markings_number_of_tracks_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_number_of_tracks_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_per_mutcd = qtw.QComboBox()
        self.input_signs_and_markings_per_mutcd.addItems(list_yes_no)

        self.input_signs_and_markings_posted_speed_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_posted_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_posted_speed_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_posted_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a.addItems(list_yes_no)


        self.input_signs_and_markings_railway_crossing_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a.addItems(list_yes_no)

        self.input_signs_and_markings_railway_crossing_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_railway_crossing_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_sidewalks_present = qtw.QComboBox()
        self.input_signs_and_markings_sidewalks_present.addItems(list_yes_no)

        self.input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = qtw.QComboBox()
        self.input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.input_signs_and_markings_stop_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_stop_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_stop_n_or_e_approach_same_post = qtw.QComboBox()
        self.input_signs_and_markings_stop_n_or_e_approach_same_post.addItems(list_yes_no_na)

        self.input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = qtw.QComboBox()
        self.input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.input_signs_and_markings_stop_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_stop_s_or_w_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_stop_s_or_w_approach_same_post = qtw.QComboBox()
        self.input_signs_and_markings_stop_s_or_w_approach_same_post.addItems(list_yes_no_na)

        self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present.addItems(list_yes_no)

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        # Group Labels
        #TODO self.input_gcws_warrant_private_9_3 = pass
        #TODO self.input_gcws_warrant_private_9_3_1 = pass
        #TODO self.input_gcws_warrant_private_9_3_2_a = pass
        #TODO self.input_gcws_warrant_private_9_3_2_b = pass
        #TODO self.input_gcws_warrant_private_9_3_2_c = pass
        #TODO self.input_gcws_warrant_public_9_1 = pass
        #TODO self.input_gcws_warrant_public_9_1_a = pass
        #TODO self.input_gcws_warrant_public_9_1_b = pass
        #TODO self.input_gcws_warrant_public_9_1_c = pass
        #TODO self.input_gcws_warrant_public_9_1_d_i = pass
        #TODO self.input_gcws_warrant_public_9_1_d_ii = pass
        #TODO self.input_gcws_warrant_public_9_1_d_iii = pass
        #TODO self.input_gcws_warrant_sidewalk_9_5 = pass
        #TODO self.input_gates_gcws_warrant_private_9_4_1_a = pass
        #TODO self.input_gates_gcws_warrant_private_9_4_1_b = pass
        #TODO self.input_gates_gcws_warrant_private_9_4_1_c = pass
        #TODO self.input_gates_gcws_warrant_public_9_2_1_a = pass
        #TODO self.input_gates_gcws_warrant_public_9_2_1_b = pass
        #TODO self.input_gates_gcws_warrant_public_9_2_1_c = pass
        #TODO self.input_gates_gcws_warrant_public_9_2_1_d = pass
        #TODO self.input_gates_gcws_warrant_public_9_2_1_e = pass
        #TODO self.input_gates_gcws_warrant_sidewalk_9_6 = pass
        self.input_gcws_warrants_comments = qtw.QTextEdit()

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        self.input_gcws_comments = qtw.QTextEdit()
         
        #Group LineEdits
        self.input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_n_or_e_approach_distance_from_road = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_s_or_w_approach_distance_from_road = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = qtw.QLineEdit() 
        self.input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = qtw.QLineEdit() 
        self.input_gcws_rail_crossing_warning_time_actual = qtw.QLineEdit() 

        #Group ComboBox
        self.input_gcws_observe_bell_if_sidewalk = qtw.QComboBox()
        self.input_gcws_observe_bell_if_sidewalk.addItems(list_yes_no)

        self.input_gcws_observe_bells_condition = qtw.QComboBox()
        self.input_gcws_observe_bells_condition.addItems(list_condition)

        self.input_gcws_observe_bells_n_or_e_approach = qtw.QComboBox()
        self.input_gcws_observe_bells_n_or_e_approach.addItems(list_yes_no)

        self.input_gcws_observe_bells_s_or_w_approach = qtw.QComboBox()
        self.input_gcws_observe_bells_s_or_w_approach.addItems(list_yes_no)

        self.input_gcws_observe_cantilever_lights_condition = qtw.QComboBox()
        self.input_gcws_observe_cantilever_lights_condition.addItems(list_condition)

        self.input_gcws_observe_cantilever_lights_n_or_e_approach = qtw.QComboBox()
        self.input_gcws_observe_cantilever_lights_n_or_e_approach.addItems(list_yes_no)

        self.input_gcws_observe_cantilever_lights_s_or_w_approach = qtw.QComboBox()
        self.input_gcws_observe_cantilever_lights_s_or_w_approach.addItems(list_yes_no)

        self.input_gcws_observe_gates_condition = qtw.QComboBox()
        self.input_gcws_observe_gates_condition.addItems(list_condition)

        self.input_gcws_observe_gates_n_or_e_approach = qtw.QComboBox()
        self.input_gcws_observe_gates_n_or_e_approach.addItems(list_yes_no)

        self.input_gcws_observe_gates_s_or_w_approach = qtw.QComboBox()
        self.input_gcws_observe_gates_s_or_w_approach.addItems(list_yes_no)

        self.input_gcws_observe_gcws_limited_use_with_walk_light_assembly = qtw.QComboBox()
        self.input_gcws_observe_gcws_limited_use_with_walk_light_assembly.addItems(list_yes_no_na)

        self.input_gcws_observe_gcws_limited_use_without_walk_light_assembly = qtw.QComboBox()
        self.input_gcws_observe_gcws_limited_use_without_walk_light_assembly.addItems(list_yes_no_na)

        self.input_gcws_observe_light_units_condition = qtw.QComboBox()
        self.input_gcws_observe_light_units_condition.addItems(list_condition)

        self.input_gcws_observe_light_units_n_or_e_approach = qtw.QComboBox()
        self.input_gcws_observe_light_units_n_or_e_approach.addItems(list_yes_no)

        self.input_gcws_observe_light_units_s_or_w_approach = qtw.QComboBox()
        self.input_gcws_observe_light_units_s_or_w_approach.addItems(list_yes_no)

        self.input_gcws_observe_warning_time_consistency = qtw.QComboBox()
        self.input_gcws_observe_warning_time_consistency.addItems(list_yes_no_na)
        
        self.input_gcws_observe_warning_time_consistency_reduced_speed = qtw.QComboBox()
        self.input_gcws_observe_warning_time_consistency_reduced_speed.addItems(list_yes_no_na)

        self.input_gcws_rail_cut_out_circuit_requirements = qtw.QComboBox()
        self.input_gcws_rail_cut_out_circuit_requirements.addItems(list_yes_no_na)

        self.input_gcws_rail_directional_stick_circuit_requirements = qtw.QComboBox()
        self.input_gcws_rail_directional_stick_circuit_requirements.addItems(list_yes_no_na)

        self.input_gcws_rail_self_diagnostic = qtw.QComboBox()
        self.input_gcws_rail_self_diagnostic.addItems(list_yes_no_na)

        #Group Labels
        #TODO self.input_gcws_rail_design_approach_warning_time = pass
        #TODO self.input_gcws_rail_design_warning_time_adjacent_crossing = pass
        #TODO self.input_gcws_rail_design_warning_time_clearance_distance = pass
        #TODO self.input_gcws_rail_design_warning_time_departure_time_pedestrian = pass
        #TODO self.input_gcws_rail_design_warning_time_departure_time_vehicle = pass
        #TODO self.input_gcws_rail_design_warning_time_gate_arm_clearance = pass
        #TODO self.input_gcws_rail_design_warning_time_preemption = pass
        #TODO self.input_gcws_rail_design_warning_time_ssd = pass

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        self.input_light_units_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_n_or_e_approach_dl = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_n_or_e_approach_dr = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_n_or_e_approach_height = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_s_or_w_approach_dl = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_s_or_w_approach_dr = qtw.QLineEdit() 
        self.input_light_units_measure_cantilevers_s_or_w_approach_height = qtw.QLineEdit() 
        self.input_light_units_measure_n_or_e_approach_height = qtw.QLineEdit() 
        self.input_light_units_measure_s_or_w_approach_height = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_light_units_observe_cantilevers_per_fig_12_3 = qtw.QComboBox()
        self.input_light_units_observe_cantilevers_per_fig_12_3.addItems(list_yes_no_na)

        self.input_light_units_observe_per_fig_12_1 = qtw.QComboBox()
        self.input_light_units_observe_per_fig_12_1.addItems(list_yes_no_na)

        self.input_light_units_observe_sidewalks_n_or_e_approach = qtw.QComboBox()
        self.input_light_units_observe_sidewalks_n_or_e_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_sidewalks_s_or_w_approach = qtw.QComboBox()
        self.input_light_units_observe_sidewalks_s_or_w_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_supplemental_lights_n_or_e_approach = qtw.QComboBox()
        self.input_light_units_observe_supplemental_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_supplemental_lights_s_or_w_approach = qtw.QComboBox()
        self.input_light_units_observe_supplemental_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_visibility_back_lights_n_or_e_approach = qtw.QComboBox()
        self.input_light_units_observe_visibility_back_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_visibility_back_lights_s_or_w_approach = qtw.QComboBox()
        self.input_light_units_observe_visibility_back_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_visibility_front_lights_n_or_e_approach = qtw.QComboBox()
        self.input_light_units_observe_visibility_front_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.input_light_units_observe_visibility_front_lights_s_or_w_approach = qtw.QComboBox()
        self.input_light_units_observe_visibility_front_lights_s_or_w_approach.addItems(list_yes_no_na)

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        self.input_gates_gcws_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = qtw.QLineEdit() 
        self.input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = qtw.QLineEdit() 
        self.input_gates_gcws_measure_gate_ascent_time = qtw.QLineEdit() 
        self.input_gates_gcws_measure_gate_descent_time = qtw.QLineEdit() 
        self.input_gates_gcws_rail_gate_arm_delay_time_design = qtw.QLineEdit() 
        self.input_gates_gcws_rail_gate_arm_descent_time_design = qtw.QLineEdit() 
        self.input_gates_gcws_rail_inner_gate_arm_delay_time_design = qtw.QLineEdit() 

        #Group Labels
        #TODO self.input_gates_gcws_calculate_gate_arm_clearance_time_recommended = pass
        #TODO self.input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = pass

        #Group ComboBoxes
        self.input_gates_gcws_observe_gate_arm_rest = qtw.QComboBox()
        self.input_gates_gcws_observe_gate_arm_rest.addItems(list_yes_no_na)

        self.input_gates_gcws_observe_gate_ascent_time = qtw.QComboBox()
        self.input_gates_gcws_observe_gate_ascent_time.addItems(list_yes_no_na)

        self.input_gates_gcws_observe_gate_descent_time = qtw.QComboBox()
        self.input_gates_gcws_observe_gate_descent_time.addItems(list_yes_no_na)

        self.input_gates_gcws_observe_gate_strips_n_or_e_approach = qtw.QComboBox()
        self.input_gates_gcws_observe_gate_strips_n_or_e_approach.addItems(list_yes_no_na)

        self.input_gates_gcws_observe_gate_strips_s_or_w_approach = qtw.QComboBox()
        self.input_gates_gcws_observe_gate_strips_s_or_w_approach.addItems(list_yes_no_na)

        self.input_gates_gcws_observe_per_fig_12_2 = qtw.QComboBox()
        self.input_gates_gcws_observe_per_fig_12_2.addItems(list_yes_no_na)

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        self.input_aawd_comments = qtw.QTextEdit()

        #Group LineEdits
        self.input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = qtw.QLineEdit() 
        self.input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = qtw.QLineEdit() 

        #Group ComboBoxes
        self.input_aawd_observe_present_n_or_e_approach = qtw.QComboBox()
        self.input_aawd_observe_present_n_or_e_approach.addItems(list_yes_no)

        self.input_aawd_observe_present_s_or_w_approach = qtw.QComboBox()
        self.input_aawd_observe_present_s_or_w_approach.addItems(list_yes_no)

        self.input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = qtw.QComboBox()
        self.input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = qtw.QComboBox()
        self.input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach.addItems(list_yes_no_na)

        #Group Labels
        #TODO self.input_aawd_calculate_advance_activation_time_design_n_or_e_approach = pass
        #TODO self.input_aawd_calculate_advance_activation_time_design_s_or_w_approach = pass
        #TODO self.input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = pass
        #TODO self.input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = pass
        #TODO self.input_aawd_warrant_gcr_lookup_road_classification = pass
        #TODO self.input_aawd_warrant_gcr_observe_environmental_condition = pass
        #TODO self.input_aawd_warrant_gcr_observe_sightline_obstruction = pass
        #TODO self.input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = pass
        #TODO self.input_aawd_warrant_mutcd_lookup_significant_road_downgrade = pass

        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        self.input_preemption_of_traffic_signals_comments = qtw.QTextEdit()
    
        #Group LineEdits
        self.input_preemption_of_traffic_signals_road_preemption_warning_time_actual = qtw.QLineEdit() 
        self.input_preemption_of_traffic_signals_road_preemption_warning_time_design = qtw.QLineEdit() 

        #Group CombBoxes
        self.input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles.addItems(list_yes_no)

        self.input_preemption_of_traffic_signals_observe_known_queuing_issues = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_known_queuing_issues.addItems(list_yes_no)

        self.input_preemption_of_traffic_signals_observe_pedestrian_accommodation = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_pedestrian_accommodation.addItems(list_yes_no_na)

        self.input_preemption_of_traffic_signals_observe_queuing_condition = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_queuing_condition.addItems(list_yes_no)

        self.input_preemption_of_traffic_signals_observe_supplemental_signage = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_supplemental_signage.addItems(list_yes_no_na)

        self.input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate.addItems(list_yes_no_na)

        self.input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals.addItems(list_yes_no_na)

        self.input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = qtw.QComboBox()
        self.input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type.addItems(list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)

        #Group DatePicker
        #TODO self.input_preemption_of_traffic_signals_road_date_Last_preemption_check = pass

        #Group Labels
        #TODO self.input_preemption_of_traffic_signals_lookup_proximity_condition = pass
        #TODO self.input_preemption_of_traffic_signals_lookup_required = pass

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        self.input_areas_without_train_whistling_comments = qtw.QTextEdit()

        #Group ComboBoxes
        self.input_areas_without_train_whistling_observe_for_stop_and_proceed = qtw.QComboBox()
        self.input_areas_without_train_whistling_observe_for_stop_and_proceed.addItems(list_yes_no_na)

        self.input_areas_without_train_whistling_observe_trespassing_area = qtw.QComboBox()
        self.input_areas_without_train_whistling_observe_trespassing_area.addItems(list_yes_no)

        self.input_areas_without_train_whistling_rail_anti_whistling_zone = qtw.QComboBox()
        self.input_areas_without_train_whistling_rail_anti_whistling_zone.addItems(list_yes_no)

        self.input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = qtw.QComboBox()
        self.input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs.addItems(list_yes_no)

        #Group Labels
        #TODO self.input_areas_without_train_whistling_lookup_gcs_12_to_16 = pass
        #TODO self.input_areas_without_train_whistling_lookup_gcs_9_2 = pass
        #TODO self.input_areas_without_train_whistling_requirements_observe_table_D1 = pass
        

        ##################
        # Layout Objects #
        ##################
        main_layout = qtw.QGridLayout()
        self.toolbox = qtw.QToolBox()
        self.setLayout(main_layout)
        main_layout.addWidget(self.toolbox, 0, 0)

        styleSheet = """
                        QToolBox::tab {
                            border: 1px solid #C4C4C3;
                            border-bottom-color: RGB(0, 0, 255);
                        }

                        QToolBox::tab:selected {
                            background-color: #f14040;
                            border-bottom-style: none;
                        }
                     """ 

        # QWidgets - Create a self.container widget
        self.container_inspection_details = qtw.QWidget(self)
        self.container_collision_history = qtw.QWidget(self)
        self.container_general_information = qtw.QWidget(self)
        self.container_design_considerations = qtw.QWidget(self)
        self.container_location_of_crossing = qtw.QWidget(self)
        self.container_crossing_surface = qtw.QWidget(self)
        self.container_road_geometry = qtw.QWidget(self)
        self.container_sightlines = qtw.QWidget(self)
        self.container_signs_and_pavement_markings = qtw.QWidget(self)
        self.container_gcws_warrants = qtw.QWidget(self)
        self.container_gcws = qtw.QWidget(self)
        self.container_gcws_lights = qtw.QWidget(self)
        self.container_gcws_gates = qtw.QWidget(self)
        self.container_aaws = qtw.QWidget(self)
        self.container_interconnection_traffic_signals = qtw.QWidget(self)
        self.container_whistle_cessation = qtw.QWidget(self)
        self.container_whistle_cessation = qtw.QWidget(self)

        #QFormLayout - Create a self.form layout
        self.form_layout_inspection_details = qtw.QFormLayout()
        self.form_layout_collision_history = qtw.QFormLayout()
        self.form_layout_general_information = qtw.QFormLayout()
        self.form_layout_design_considerations = qtw.QFormLayout()
        self.form_layout_location_of_crossing = qtw.QFormLayout()
        self.form_layout_crossing_surface = qtw.QFormLayout()
        self.form_layout_road_geometry = qtw.QFormLayout()
        self.form_layout_sightlines = qtw.QFormLayout()
        self.form_layout_signs_and_pavement_markings = qtw.QFormLayout()
        self.form_layout_gcws_warrants = qtw.QFormLayout()
        self.form_layout_gcws = qtw.QFormLayout()
        self.form_layout_gcws_lights = qtw.QFormLayout()
        self.form_layout_gcws_gates = qtw.QFormLayout()
        self.form_layout_aaws = qtw.QFormLayout()
        self.form_layout_interconnection_traffic_signals = qtw.QFormLayout()
        self.form_layout_whistle_cessation = qtw.QFormLayout()

        #Set Form Layouts to Container Widgets
        self.container_inspection_details.setLayout(self.form_layout_inspection_details)        
        self.container_collision_history.setLayout(self.form_layout_collision_history)
        self.container_general_information.setLayout(self.form_layout_general_information)
        self.container_design_considerations.setLayout(self.form_layout_design_considerations)
        self.container_location_of_crossing.setLayout(self.form_layout_location_of_crossing)
        self.container_crossing_surface.setLayout(self.form_layout_crossing_surface)
        self.container_road_geometry.setLayout(self.form_layout_road_geometry)
        self.container_sightlines.setLayout(self.form_layout_sightlines)
        self.container_signs_and_pavement_markings.setLayout(self.form_layout_signs_and_pavement_markings)
        self.container_gcws_warrants.setLayout(self.form_layout_gcws_warrants)
        self.container_gcws.setLayout(self.form_layout_gcws)
        self.container_gcws_lights.setLayout(self.form_layout_gcws_lights)
        self.container_gcws_gates.setLayout(self.form_layout_gcws_gates)
        self.container_aaws.setLayout(self.form_layout_aaws)
        self.container_interconnection_traffic_signals.setLayout(self.form_layout_interconnection_traffic_signals)
        self.container_whistle_cessation.setLayout(self.form_layout_whistle_cessation)

        #Add Container Widgets to Toolbox
        self.toolbox.addItem(self.container_inspection_details, 'INSPECTION DETAILS')
        self.toolbox.addItem(self.container_collision_history, 'COLLISION HISTORY (5 YEAR PERIOD)')
        self.toolbox.addItem(self.container_general_information, 'GENERAL INFORMATION')
        self.toolbox.addItem(self.container_design_considerations, 'DESIGN CONSIDERATIONS (GCS SECTION 10)')
        self.toolbox.addItem(self.container_location_of_crossing, 'LOCATION OF GRADE CROSSING (GCS SECTION 11)')
        self.toolbox.addItem(self.container_crossing_surface, 'CROSSING SURFACE (GCS SECTION 5)')
        self.toolbox.addItem(self.container_road_geometry, 'ROAD GEOMETRY (GCS SECTION 6)')
        self.toolbox.addItem(self.container_sightlines, 'SIGHTLINES (GCS SECTION 7)')
        self.toolbox.addItem(self.container_signs_and_pavement_markings, 'SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)')
        self.toolbox.addItem(self.container_gcws_warrants, 'GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)')
        self.toolbox.addItem(self.container_gcws, 'GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)')
        self.toolbox.addItem(self.container_gcws_lights, 'FLASHING LIGHT UNITS (GCS SECTION 13 & 14)')
        self.toolbox.addItem(self.container_gcws_gates, 'GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)')
        self.toolbox.addItem(self.container_aaws, 'PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)')
        self.toolbox.addItem(self.container_interconnection_traffic_signals, 'INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)')
        self.toolbox.addItem(self.container_whistle_cessation, 'WHISTLE CESSATION (GCS SECTION Appendix D)')

        self.toolbox.setCurrentIndex(1)
        self.toolbox.setStyleSheet(styleSheet)
        
        # layout self.container widgets - INSPECTION DETAILS
        #TODO self.form_layout_inspection_details.addRow('Date of Assessment:', self.input_inspection_details_date_assessment)
        self.form_layout_inspection_details.addRow('Assessment Team Members & Affiliations:', self.input_inspection_details_assessment_team)
        self.form_layout_inspection_details.addRow('Reason for Assessment:', self.input_inspection_details_reason_for_assessment)
        self.form_layout_inspection_details.addRow('Railway Authority:', self.input_inspection_details_railway_authority)
        self.form_layout_inspection_details.addRow('Crossing Location:', self.input_inspection_details_crossing_location)
        self.form_layout_inspection_details.addRow('Location Number:', self.input_inspection_details_location_number)
        self.form_layout_inspection_details.addRow('Subdivision Name:', self.input_inspection_details_subdivision_name)
        self.form_layout_inspection_details.addRow('Subdivision Mile:', self.input_inspection_details_subdivision_mile)
        self.form_layout_inspection_details.addRow('Spur Name:', self.input_inspection_details_spur_name)
        self.form_layout_inspection_details.addRow('Spur Mile:', self.input_inspection_details_spur_mile)
        self.form_layout_inspection_details.addRow('Type of Crossing:', self.input_inspection_details_grade_crossing_type)     
        self.form_layout_inspection_details.addRow('Type of Protection:', self.input_inspection_details_gcws_type)
        self.form_layout_inspection_details.addRow('Track Type:', self.input_inspection_details_track_type)
        self.form_layout_inspection_details.addRow('Road Authority:', self.input_inspection_details_road_authority)
        self.form_layout_inspection_details.addRow('Municipality:', self.input_inspection_details_municipality)
        self.form_layout_inspection_details.addRow('Road Name:', self.input_inspection_details_road_name)   
        self.form_layout_inspection_details.addRow('Road Number:', self.input_inspection_details_road_number)
        self.form_layout_inspection_details.addRow('Province:', self.input_inspection_details_province)     
        self.form_layout_inspection_details.addRow('Latitude:', self.input_inspection_details_latitude)
        self.form_layout_inspection_details.addRow('Longitude:', self.input_inspection_details_longitude)

        # layout self.container widgets - COLLISION HISTORY (5 YEAR PERIOD)
        self.form_layout_collision_history.addRow('Property Damage Collisions:', self.input_collision_history_property_damage)
        self.form_layout_collision_history.addRow('Personal Injury Collisions:', self.input_collision_history_personal_injury)
        self.form_layout_collision_history.addRow('Fatal Injury Collisions:', self.input_collision_history_fatal_injury)
        #self.form_layout_collision_history.addRow('Total Collisions in the last 5 year period:', self.input_collision_history_total_5_year_period)
        self.form_layout_collision_history.addRow('Number of Persons Injured:', self.input_collision_history_fatalities)
        self.form_layout_collision_history.addRow('Number of Persons Killed:', self.input_collision_history_personal_injuries)
        self.form_layout_collision_history.addRow('Details of Collisions:', self.input_collision_history_comments)

        # layout self.container widgets - GENERAL INFORMATION
        self.form_layout_general_information.addRow('Maximum Freight Railway Operating Speed (mph)', self.input_general_info_rail_max_railway_operating_speed_freight)
        self.form_layout_general_information.addRow('Maximum Passenger Railway Operating Speed (mph)', self.input_general_info_rail_max_railway_operating_speed_passenger)
        self.form_layout_general_information.addRow('Railway Design Speed, VT (mph)', self.input_general_info_rail_railway_design_speed)
        self.form_layout_general_information.addRow('Freight Trains/Day:', self.input_general_info_rail_no_trains_per_day_freight)
        self.form_layout_general_information.addRow('Passenger Trains/Day:', self.input_general_info_rail_no_trains_per_day_passengers)
        #TODO self.form_layout_general_information.addRow('Total Trains/Day:', self.input_general_info_rail_no_trains_per_day_total)
        #TODO self.form_layout_general_information.addRow('Number of Tracks', self.input_general_info_rail_no_tracks_total)
        self.form_layout_general_information.addRow('Train Switching within Crossing Approaches?', self.input_general_info_rail_train_switching)
        self.form_layout_general_information.addRow('Road Crossing Design Speed (km/hr)', self.input_general_info_road_speed_design)
        self.form_layout_general_information.addRow('Road Posted Speed (km/hr)', self.input_general_info_road_speed_posted)
        self.form_layout_general_information.addRow('Current Average Annual Daily Traffic, AADT', self.input_general_info_road_aadt_current)
        self.form_layout_general_information.addRow('Year of Count:', self.input_general_info_road_aadt_year_current)
        self.form_layout_general_information.addRow('Forecasted Average Annual Daily Traffic, AADT', self.input_general_info_road_aadt_forecast)
        self.form_layout_general_information.addRow('Forecast Year:', self.input_general_info_road_aadt_year_forecasted)
        self.form_layout_general_information.addRow('Pedestrian Volume per Day', self.input_general_info_road_pedestrians_per_day)
        self.form_layout_general_information.addRow('Cyclist Volume per Day', self.input_general_info_road_cyclist_per_day)
        self.form_layout_general_information.addRow('Northbound / Eastbound', self.input_general_info_road_no_traffic_lanes_northbound_or_eastbound)
        self.form_layout_general_information.addRow('Southbound / Westbound', self.input_general_info_road_no_traffic_lanes_southbound_or_westbound)
        self.form_layout_general_information.addRow('Bidirectional', self.input_general_info_road_no_traffic_lanes_bidirectional)
        #TODO self.form_layout_general_information.addRow('Total', self.input_general_info_road_no_traffic_lanes_total)
        self.form_layout_general_information.addRow('Does Grade Crossing Include sidewalk, Path, or Trail?', self.input_general_info_road_sidewalks)
        self.form_layout_general_information.addRow('Regular Use of Crossing by Persons with Assistive Devices?', self.input_general_info_road_assistive_pedestrian_devices)
        self.form_layout_general_information.addRow('High Seasonal Fluctuation in Volumes?', self.input_general_info_road_seasonal_volume_fluctuations)
        self.form_layout_general_information.addRow('Is Crossing on a School Bus Route?', self.input_general_info_road_school_bus_route)
        self.form_layout_general_information.addRow('Do Dangerous Goods Trucks Use this Roadway?', self.input_general_info_road_dangerous_goods_route)
        self.form_layout_general_information.addRow('Other Special Road Users?', self.input_general_info_road_other_users)
        self.form_layout_general_information.addRow('Volume', self.input_general_info_road_other_users_daily_users)
        self.form_layout_general_information.addRow('Surrounding Land Use:', self.input_general_info_observe_surrounding_land_use)
        self.form_layout_general_information.addRow('Any schools, retirement homes, etc. nearby?', self.input_general_info_observe_special_buildings)
        self.form_layout_general_information.addRow('Urban/rural?', self.input_general_info_road_classification)
        self.form_layout_general_information.addRow('roadway Illumination?', self.input_general_info_observe_roadway_illumination)
        self.form_layout_general_information.addRow('Comments Regarding General Inself.formation', self.input_general_info_comments)

        # layout self.container widgets - DESIGN CONSIDERATIONS (GCS SECTION 10)
        self.form_layout_design_considerations.addRow('Design Vehicle Type:', self.input_design_road_design_vehicle_type)
        #TODO self.form_layout_design_considerations.addRow('Design Vehicle Class:', self.input_design_lookup_design_vehicle_class)
        #TODO self.form_layout_design_considerations.addRow('Design Vehicle Length (m):', self.input_design_lookup_design_vehicle_length)
        self.form_layout_design_considerations.addRow('Clearance Distance - Vehicle, cd (m):', self.input_design_measure_clearance_distance_vehicle)
        #TODO self.form_layout_design_considerations.addRow('Vehicle Travel Distance, S = L + cd (m):', self.input_design_calculate_vehicle_travel_distance)
        #TODO self.form_layout_design_considerations.addRow('Departure Time - Vehicle, Td = J + T:', self.input_design_calculate_clearance_time_crossing_vehicle_design_check)
        #TODO self.form_layout_design_considerations.addRow("Driver's Reaction Time (s):", self.input_design_self.input_reaction_time)
        self.form_layout_design_considerations.addRow('Maximum Road Approach Grade within S (%):', self.input_design_road_max_approach_grade_within_s)
        #TODO self.form_layout_design_considerations.addRow('Grade Adjustment Factor:', self.input_design_lookup_grade_adjustment_factor)
        self.form_layout_design_considerations.addRow('Do Field Acceleration Times Exceed Td?:', self.input_design_observe_field_acceleration_times_exceed_td)
        self.form_layout_design_considerations.addRow('Clearance Distance - Pedestrian, cd (m):', self.input_design_measure_clearance_distance_pedestrian)
        #TODO self.form_layout_design_considerations.addRow('Departure Time - Pedestrian, Td = J + T:', self.input_design_calculate_clearance_time_crossing_pedestrian_design_check)
        self.form_layout_design_considerations.addRow('Separation Distnace Between Adjacent Tracks (m):', self.input_design_measure_adjacent_track_separation_distance)      
        self.form_layout_design_considerations.addRow('Adjacent Track Clearance Distance (m):', self.input_design_measure_adjacent_track_clearance_distance)
        #TODO self.form_layout_design_considerations.addRow('Adjacent Track Clearance Time (s):', self.input_design_calculate_adjacent_track_clearance_time)
        #TODO self.form_layout_design_considerations.addRow('', self.input_design_calculate_clearance_time_gate_arm_ssd)
        #TODO self.form_layout_design_considerations.addRow('', self.input_design_calculate_clearance_time_gate_arm_stop)
        #TODO self.form_layout_design_considerations.addRow('', self.input_design_lookup_vehicle_departure_time_crossing)
        #TODO self.form_layout_design_considerations.addRow('', self.input_design_lookup_vehicle_departure_time_gate_arm_clearance)        
        #TODO self.form_layout_design_considerations.addRow('Design Consideration Comments', self.input_design_comments)

        # layout self.container widgets - LOCATION OF GRADE CROSSING (GCS SECTION 11)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('D (Intersection with Stop Sign)'))
        self.form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach)
        self.form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('D (Signalized Intersection)'))
        self.form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach)
        self.form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('D (Other Intersection / Driveway / Crosswalk)'))
        self.form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach)
        self.form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach)        
        self.form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles might queue onto the tracks?:', self.input_location_of_grade_crossing_queue_condition)
        self.form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles turning from a side street might not see warning devices for the crossing?:', self.input_location_of_grade_crossing_visibility_of_warning_lights)
        self.form_layout_location_of_crossing.addRow('Are there pedestrian crossings on either road approach that could cause vehicles to queue back to the tracks?:', self.input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk)
        self.form_layout_location_of_crossing.addRow('Location of Grade Crossing Comments:', self.input_location_of_grade_crossing_comments)

        # layout self.container widgets - GRADE CROSSING SURFACE (GCS SECTION 5)
        self.form_layout_crossing_surface.addRow('Is the crossing smooth enough to allow road vehicles, pedestrians, cyclists, and other road users to cross at their normal speed without consequence? Comments below.', self.input_grade_crossing_surface_observe_crossing_smoothness)
        self.form_layout_crossing_surface.addRow('Grade Crossing Surface Material', self.input_grade_crossing_surface_observe_material)
        self.form_layout_crossing_surface.addRow('Grade Crossing Surface Condition', self.input_grade_crossing_surface_observe_crossing_surface_condition)
        self.form_layout_crossing_surface.addRow('Road Approach Surface Type', self.input_grade_crossing_surface_observe_road_approach_surface_type)
        self.form_layout_crossing_surface.addRow('Road Approach Surface Condition', self.input_grade_crossing_surface_observe_road_approach_surface_condition)        
        self.form_layout_crossing_surface.addRow('Crossing Surface Width (m):', self.input_grade_crossing_surface_measure_crossing_surface_width)
        self.form_layout_crossing_surface.addRow('Centre Lane/Median Width (m):', self.input_grade_crossing_surface_measure_road_surface_median_width)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Travelled Way Width (m):'))
        self.form_layout_crossing_surface.addRow('N or E Road Approach:', self.input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Road Approach:', self.input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Paved Shoulder Width (m):'))
        self.form_layout_crossing_surface.addRow('N or E Rail Approach:', self.input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Rail Approach:', self.input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Surface Extension beyond Travel Lanes/Shoulder (m):'))
        self.form_layout_crossing_surface.addRow('N or E Rail Approach:', self.input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Rail Approach:', self.input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Sidewalk / Path / Trail Width (m):'))
        self.form_layout_crossing_surface.addRow('N or E Rail Approach:', self.input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Rail Approach:', self.input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Surface Extension beyond Sidewalk / Path / Trail (m):'))
        self.form_layout_crossing_surface.addRow('N or E Rail Approach:', self.input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Rail Approach:', self.input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Distance Between Travel Lane / Shoulder and Sidewalk / Path / Trail (m):'))
        self.form_layout_crossing_surface.addRow('N or E Rail Approach:', self.input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Rail Approach:', self.input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach)
        self.form_layout_crossing_surface.addRow(qtw.QLabel('Distance from path centreline to crossing warning device (m):'))
        self.form_layout_crossing_surface.addRow('N or E Rail Approach:', self.input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach)
        self.form_layout_crossing_surface.addRow('S or W Rail Approach:', self.input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach)
        self.form_layout_crossing_surface.addRow('Flangeway Depth (mm):', self.input_grade_crossing_surface_measure_flangeway_depth)
        self.form_layout_crossing_surface.addRow('Flangeway Width (mm):', self.input_grade_crossing_surface_measure_flangeway_width)
        self.form_layout_crossing_surface.addRow('Field Side Grinding Depth (mm):', self.input_grade_crossing_surface_measure_side_grinding_depth)
        self.form_layout_crossing_surface.addRow('Field Side Grinding Width (mm):', self.input_grade_crossing_surface_measure_side_grinding_width)
        self.form_layout_crossing_surface.addRow('Elevation of top of Rail Above Road Surface (mm):', self.input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface)
        self.form_layout_crossing_surface.addRow('Elevation of top of Rail Below Road Surface (mm):', self.input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface)
        self.form_layout_crossing_surface.addRow('Crossing Surface Comments:', self.input_grade_crossing_surface_comments)

        # layout self.container widgets - ROAD GEOMETRY (GCS SECTION 6)
        self.form_layout_road_geometry.addRow(qtw.QLabel('Are the horizontal and vertical alignments smooth and continuous throughout SSD?'))
        self.form_layout_road_geometry.addRow('N or E Road Approach:', self.input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach)
        self.form_layout_road_geometry.addRow('S or W Road Approach:', self.input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach)
        self.form_layout_road_geometry.addRow(qtw.QLabel('Are the road lanes and shoulders at least the same width on the crossing as on the road approaches?'))
        self.form_layout_road_geometry.addRow('N or E Road Approach:', self.input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach)
        self.form_layout_road_geometry.addRow('S or W Road Approach:', self.input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach)
        self.form_layout_road_geometry.addRow(qtw.QLabel('Road Approach Grades (%):'))
        self.form_layout_road_geometry.addRow('Within 8m (N or E Road Approach):', self.input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach)
        self.form_layout_road_geometry.addRow('Within 8m (S or W Road Approach):', self.input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach)
        self.form_layout_road_geometry.addRow('Between 8m to 18m (N or E Road Approach):', self.input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach)
        self.form_layout_road_geometry.addRow('Between 8m to 18m (S or W Road Approach):', self.input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach)
        self.form_layout_road_geometry.addRow('Across SSD (N or E Road Approach):', self.input_road_geometry_road_general_approach_grade_n_or_e_approach)
        self.form_layout_road_geometry.addRow('Across SSD (S or W Road Approach):', self.input_road_geometry_road_general_approach_grade_s_or_w_approach)
        self.form_layout_road_geometry.addRow('Within 5m of Sidewalk/Path/Trail (N or E Road Approach):', self.input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach)
        self.form_layout_road_geometry.addRow('Within 5m of Sidewalk/Path/Trail (S or W Road Approach):', self.input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach)
        #self.form_layout_road_geometry.addRow('Allowable difference between roadway gradient and railway cross-slope (%)', self.input_road_geometry_lookup_gradient_difference)
        self.form_layout_road_geometry.addRow('Railway Cross Slope (%):', self.input_road_geometry_measure_railway_cross_slope)
        self.form_layout_road_geometry.addRow('Are rail tracks super elevated? (N or E Road Approach):', self.input_road_geometry_rail_superelevation_n_or_e_approach)
        self.form_layout_road_geometry.addRow('Are rail tracks super elevated? (S or W Road Approach):', self.input_road_geometry_rail_superelevation_s_or_w_approach)
        self.form_layout_road_geometry.addRow('Is there any evidence that "low-bed" trucks have difficulty negotiating the crossing? (i.e. might they bottom-out or get stuck?)', self.input_road_geometry_observe_low_bed_truck_condition)
        self.form_layout_road_geometry.addRow('Grade Crossing Angle:', self.input_road_geometry_road_crossing_angle)
        self.form_layout_road_geometry.addRow('Road Geometry Comments:', self.input_road_geometry_comments)

        # layout self.container widgets - SIGHTLINES (GCS SECTION 7)
        #TODO self.form_layout_sightlines.addRow('SSD Minimum (N or E Road Approach) (m):', self.input_sightlines_lookup_ssd_minimum_n_or_e_approach)
        #TODO self.form_layout_sightlines.addRow('SSD Minimum (S or W Road Approach) (m):', self.input_sightlines_lookup_ssd_minimum_s_or_w_approach)
        self.form_layout_sightlines.addRow('SSD Actual (N or E Road Approach) (m):', self.input_sightlines_measure_ssd_actual_n_or_e_approach)
        self.form_layout_sightlines.addRow('SSD Actual (S or W Road Approach) (m):', self.input_sightlines_measure_ssd_actual_s_or_w_approach)
        #TODO self.form_layout_sightlines.addRow('DSSD Minimum (ft):', self.input_sightlines_calculate_Dssd_vehicle_Min_ft)
        #TODO self.form_layout_sightlines.addRow('DSSD Minimum (m):', self.input_sightlines_calculate_Dssd_vehicle_Min_m)
        self.form_layout_sightlines.addRow("DSSD Actual (N or E Road Approach) (Driver's Left) (m):", self.input_sightlines_measure_dssd_actual_n_or_e_approach_left)
        self.form_layout_sightlines.addRow("DSSD Actual (N or E Road Approach) (Driver's Right) (m):", self.input_sightlines_measure_dssd_actual_n_or_e_approach_right)
        self.form_layout_sightlines.addRow("DSSD Actual (S or W Road Approach) (Driver's Left) (m):", self.input_sightlines_measure_dssd_actual_s_or_w_approach_left)
        self.form_layout_sightlines.addRow("DSSD Actual (S or W Road Approach) (Driver's Right) (m):", self.input_sightlines_measure_dssd_actual_s_or_w_approach_right)
        #TODO self.form_layout_sightlines.addRow('DStopped Minimum (Vehicle) (ft):', self.input_sightlines_calculate_Dstopped_vehicle_Min_ft)
        #TODO self.form_layout_sightlines.addRow('DStopped Minimum (Vehicle) (m):', self.input_sightlines_calculate_Dstopped_vehicle_Min_m)
        #TODO self.form_layout_sightlines.addRow('DStopped Minimum (Pedestiran) (ft):', self.input_sightlines_calculate_Dstopped_pedestrian_Min_ft)
        #TODO self.form_layout_sightlines.addRow('DStopped Minimum (Pedestrian) (m):', self.input_sightlines_calculate_Dstopped_pedestrian_Min_m)
        self.form_layout_sightlines.addRow("DStopped Actual (N or E Road Approach) (Driver's Left) (m):", self.input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left)
        self.form_layout_sightlines.addRow("DStopped Actual (N or E Road Approach) (Driver's Right) (m):", self.input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right)
        self.form_layout_sightlines.addRow("DStopped Actual (S or W Road Approach) (Driver's Left) (m):", self.input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left)
        self.form_layout_sightlines.addRow("DStopped Actual (S or W Road Approach) (Driver's Right) (m):", self.input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right)
        self.form_layout_sightlines.addRow("Are there any obstacles within the sight triangles that affect visibility?", self.input_sightlines_observe_sightline_obstructions)
        self.form_layout_sightlines.addRow(qtw.QLabel("Examples: Building(s), Rail/Road Alignment, Commercial Signing, Unattended Railway Equipment, Topography, Traffic Control Devices, Utilities, Vegetation)"))
        self.form_layout_sightlines.addRow('Sightline Comments', self.input_sightlines_comments)

        # layout self.container widgets - SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_advisory_speed_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_advisory_speed_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_advisory_speed_s_or_w_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_dividing_lines_present)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_comments
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_n_or_e_approach_condition)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_n_or_e_approach_legible)
        #TODO self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_n_or_e_approach_orientation)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_s_or_w_approach_condition)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_s_or_w_approach_legible)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_s_or_w_approach_orientation)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_emergency_notification_s_or_w_approach_present)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_number_of_tracks_s_or_w_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_per_mutcd)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_posted_speed_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_posted_speed_s_or_w_approach_present)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_railway_crossing_s_or_w_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_sidewalks_present)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_n_or_e_approach_height)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_n_or_e_approach_location_from_rail)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_n_or_e_approach_location_from_road)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_n_or_e_approach_same_post)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_s_or_w_approach_height)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_s_or_w_approach_location_from_rail)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_s_or_w_approach_location_from_road)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_s_or_w_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_s_or_w_approach_same_post)
        #DELETE self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_comments)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road)
        self.form_layout_signs_and_pavement_markings.addRow('', self.input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present)

        # layout self.container widgets - GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Public Crossings)'))
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('If any of A through D below are met, then a warning system without gates is required'))
        #TODO self.form_layout_gcws_warrants.addRow("A. Where the forecast cross-product is 2,000 or more:"", self.input_gcws_warrant_public_9_1_a)
        #TODO self.form_layout_gcws_warrants.addRow("B. Where there is no sidewalk, path or trail and the railway design speed is more than 129 km/hr (80 mph);", self.input_gcws_warrant_public_9_1_b)
        #TODO self.form_layout_gcws_warrants.addRow("C. Where there is a sidewalk, path or trail and the railway design speed is more than 81 km/hr (50 mph);", self.input_gcws_warrant_public_9_1_c)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('D. Where the railway design speed is more than 25 km/hr (15 mph) but less than the railway design speed referred to in (b) or (c), and'))
        #TODO self.form_layout_gcws_warrants.addRow("D1. Where there are two or more lines of railway where railway equipment may pass each other;", self.input_gcws_warrant_public_9_1_d_i)
        #TODO self.form_layout_gcws_warrants.addRow("D2. The distance as shown in Figure 9-1(a) between a Stop sign at an intersection and the nearest rail in the crossing surface is less than 30m;", self.input_gcws_warrant_public_9_1_d_ii)
        #TODO self.form_layout_gcws_warrants.addRow("D3. In the case of an intersection with a traffic signal, the distance between the stop line of the intersection and the nearest rail in the crossing surface, as shown in Figure 9-1(b), is less than 60m, or where there is no stop line, the distance between the travelled way and the nearest rail in the crossing surface is less than 60m.", self.input_gcws_warrant_public_9_1_d_iii)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Private Crossings)'))
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('If any of A through B below are met, then a warning system without gates is required'))
        #TODO self.form_layout_gcws_warrants.addRow("A. Where the forecast cross-product is 2,000 or more;", self.input_gcws_warrant_private_9_3_1)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('B. Where the railway design speed is more than 25 km/hr (15mph), and;'))
        #TODO self.form_layout_gcws_warrants.addRow("B1. The forecast cross-product is 100 or more and there are two or more lines of railway where railway equipment may pass each other;", self.input_gcws_warrant_private_9_3_2_a)
        #TODO self.form_layout_gcws_warrants.addRow("B2. The forecast cross-product is 100 or more and grade crossing does not include a sidewalk, path or trail and the railway design speed is more than 129 km/hr (80mph);", self.input_gcws_warrant_private_9_3_2_b)
        #TODO self.form_layout_gcws_warrants.addRow("B3. The grade crossing does includes a sidewalk, path or trail and the railway design speed is more than 81 km/hr (50mph);", self.input_gcws_warrant_private_9_3_2_c)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Grade Crossings for a Sidewalk, Path, or Trail)'))
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('If A below is met, then a warning system without gates is required'))
        #TODO self.form_layout_gcws_warrants.addRow("A. The sidewalk, path or trail is outside the island circuit of an adjacent warning system and the railway design speed is more than 81 km/hr (50mph)", self.input_gcws_warrant_sidewalk_9_5)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Public Crossings)'))
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('If a warning system is warranted, and any of A through F are met, then gates are also required'))
        #TODO self.form_layout_gcws_gates.addRow("A. A warning system is required under 9.1, and;", self.input_gcws_warrant_public_9_1)
        #TODO self.form_layout_gcws_gates.addRow("B. The forecast cross-product is 50,000 or more;", self.input_gates_gcws_warrant_public_9_2_1_a)
        #TODO self.form_layout_gcws_gates.addRow("C. There are two or more lines of railway where railway equipment may pass each other;", self.input_gates_gcws_warrant_public_9_2_1_b)
        #TODO self.form_layout_gcws_gates.addRow("D. The railway design speed is more than 81 km/hr (50mph);", self.input_gates_gcws_warrant_public_9_2_1_c)
        #TODO self.form_layout_gcws_gates.addRow("E. The distance as shown in Figure 9-1(a) between a Stop sign at an intersection and the nearest rail in the crossing surface is less than 30m;", self.input_gates_gcws_warrant_public_9_2_1_d)
        #TODO self.form_layout_gcws_gates.addRow("F. In the case of an intersection with a traffic signal, the distance between the stop line of the intersection and the nearest rail in the crossing surface, as shown in Figure 9-1(b), is less than 60m, or where there is no stop line, the distance between the travelled way and the nearest rail in the crossing surface is less than 60m.", self.input_gates_gcws_warrant_public_9_2_1_e)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Private Crossings)'))
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('If a warning system is warranted, and any of A through D are met, then gates are also required'))
        #TODO self.form_layout_gcws_gates.addRow("A. A warning system is required under 9.1, and;", self.input_gcws_warrant_private_9_3)
        #TODO self.form_layout_gcws_gates.addRow("B. The forecast cross-product is 50,000 or more;", self.input_gates_gcws_warrant_private_9_4_1_a)
        #TODO self.form_layout_gcws_gates.addRow("C. There are two or more lines of railway where railway equipment may pass each other;", self.input_gates_gcws_warrant_private_9_4_1_b)
        #TODO self.form_layout_gcws_gates.addRow("D. The railway design speed is more than 81 km/hr (50mph);", self.input_gates_gcws_warrant_private_9_4_1_c)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Grade Crossings for a Sidewalk, Path, or Trail)'))
        #TODO self.form_layout_gcws_gates.addRow("", self.input_gates_gcws_warrant_sidewalk_9_6)
        self.form_layout_gcws_warrants.addRow('GCWS Warrants Comments', self.input_gcws_warrants_comments)

        # layout self.container widgets - GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #TODO self.form_layout_gcws.addRow('Design Approach Warning Time:', self.input_gcws_rail_design_approach_warning_time)
        self.form_layout_gcws_warrants.addRow(qtw.QLabel('Should be greatest of:'))
        #TODO self.form_layout_gcws.addRow("a. 20 s, unless the grade crossing clearance distance (Fig 10-1) is more than 11 m (35 ft), in which case, the 20 s must be increased by one second for each additional 3 m (10 ft), or fraction thereof;", self.input_gcws_rail_design_warning_time_clearance_distance)
        #TODO self.form_layout_gcws.addRow("b. The Departure Time for the grade crossing "design vehicle" (Article 10.3.2);", self.input_gcws_rail_design_warning_time_departure_time_vehicle)
        #TODO self.form_layout_gcws.addRow("c. The Departure Time for pedestrians, cyclists, and persons using assistive devices (Article 10.3.3);", self.input_gcws_rail_design_warning_time_departure_time_pedestrian)
        #TODO self.form_layout_gcws.addRow("d. The gate arm clearance time, plus the time to complete the gate arm descent, plus 5 seconds;", self.input_gcws_rail_design_warning_time_gate_arm_clearance)
        #TODO self.form_layout_gcws.addRow("e. The minimum warning time required for traffic signal pre-emption;", self.input_gcws_rail_design_warning_time_preemption)
        #TODO self.form_layout_gcws.addRow("f. The time for the design vehicle travelling at the design speed to travel from the stopping sight distance, as specified in article 1.2.5.2 of the Geometric Design Guide and pass completely through the clearance distance;", self.input_gcws_rail_design_warning_time_ssd)
        #TODO self.form_layout_gcws.addRow("g. Adjacent Track Interconnected Highway-Rail Grade Crossing. (add to (a), - (e))", self.input_gcws_rail_design_warning_time_adjacent_crossing)
        self.form_layout_gcws.addRow('Actual Approach Warning Time:', self.input_gcws_rail_crossing_warning_time_actual)
        self.form_layout_gcws.addRow(qtw.QLabel("Warning Systems Clearance Distance from Railway (Min. 3.66 m (12 ft) for signal mast or 3.05 m (10 ft) for end of gate arm; from centreline of track) (m):"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail)
        self.form_layout_gcws.addRow(qtw.QLabel("Warning System Clearance Distance from Roadway (Min. 625 mm from curb; or 1.875 m from travelled way and 625 mm from shoulder) (m)"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_measure_warning_device_n_or_e_approach_distance_from_road)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_measure_warning_device_s_or_w_approach_distance_from_road)
        self.form_layout_gcws.addRow(qtw.QLabel("Distance between top of foundation and surrounding ground level (max. 100 mm (4 in))"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation)
        self.form_layout_gcws.addRow(qtw.QLabel("Is the slope of surrounding ground from foundation towards the travelled way less than 25% (4:1)?"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation)
        self.form_layout_gcws.addRow(qtw.QLabel("Light units:"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_observe_light_units_n_or_e_approach)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_observe_light_units_s_or_w_approach)
        self.form_layout_gcws.addRow('Condition:', self.input_gcws_observe_light_units_condition)
        self.form_layout_gcws.addRow(qtw.QLabel("Cantilever Lights:"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_observe_cantilever_lights_n_or_e_approach)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_observe_cantilever_lights_s_or_w_approach)
        self.form_layout_gcws.addRow('Condition:', self.input_gcws_observe_cantilever_lights_condition)
        self.form_layout_gcws.addRow('If there is only one sidewalk, is a bell located on the adjacent assembly?', self.input_gcws_observe_bell_if_sidewalk)
        self.form_layout_gcws.addRow(qtw.QLabel("Bells:"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_observe_bells_n_or_e_approach)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_observe_bells_s_or_w_approach)
        self.form_layout_gcws.addRow('Condition:', self.input_gcws_observe_bells_condition)
        self.form_layout_gcws.addRow(qtw.QLabel("Gates:"))
        self.form_layout_gcws.addRow('N or E Road Approach:', self.input_gcws_observe_gates_n_or_e_approach)
        self.form_layout_gcws.addRow('S or W Road Approach:', self.input_gcws_observe_gates_s_or_w_approach)
        self.form_layout_gcws.addRow('Condition:', self.input_gcws_observe_gates_condition)
        self.form_layout_gcws.addRow('Is crossing warning system equipped with monitoring devices that gather and retain the data and time of information (per 12.2) for a min. of 30 days?', self.input_gcws_rail_self_diagnostic)
        self.form_layout_gcws.addRow('Does crossing warning system provide consitent warning times for railway equipment regularly operating over the grade crossing?', self.input_gcws_observe_warning_time_consistency)
        self.form_layout_gcws.addRow('Where Railway Design Speed has been reduced, other than TSO, does actual Crossing Warning Time exceed 13s compared with design?', self.input_gcws_observe_warning_time_consistency_reduced_speed)
        self.form_layout_gcws.addRow('Where railway eqipment regularly stops, left standing or turnout present within limits of warning systems, are Cut-Out Circuits in place?', self.input_gcws_rail_cut_out_circuit_requirements)
        self.form_layout_gcws.addRow('If Directional Stick Circuits present, are requirments of GCS 16.4 met?', self.input_gcws_rail_directional_stick_circuit_requirements)
        self.form_layout_gcws.addRow('Limited Use Warning System without Walk Light Assembly (Y/N)? (For Private Crossing with fewer than 3 residential dwellings only)', self.input_gcws_observe_gcws_limited_use_without_walk_light_assembly)
        self.form_layout_gcws.addRow('Limited Use Warning System with Walk Light Assembly (Y/N)? (For Private Crossing and restricted access only)', self.input_gcws_observe_gcws_limited_use_with_walk_light_assembly)
        self.form_layout_gcws.addRow('GCWS Comments', self.input_gcws_comments)
        
        # layout self.container widgets - FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        self.form_layout_gcws_lights.addRow('Are signal assemblies as shown in Figure 12-1?', self.input_light_units_observe_per_fig_12_1)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Alignment Height (m):'))
        self.form_layout_gcws_lights.addRow('N or E Road Approach:', self.input_light_units_measure_n_or_e_approach_height)
        self.form_layout_gcws_lights.addRow('S or W Road Approach:', self.input_light_units_measure_s_or_w_approach_height)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Are primary light units visible for at least the minimum SSD?'))
        self.form_layout_gcws_lights.addRow('N or E Road Approach:', self.input_light_units_observe_visibility_front_lights_n_or_e_approach)
        self.form_layout_gcws_lights.addRow('S or W Road Approach:', self.input_light_units_observe_visibility_front_lights_s_or_w_approach)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Are additional light units required to cover intermediate areas of the road approaches?'))
        self.form_layout_gcws_lights.addRow('N or E Road Approach:', self.input_light_units_observe_supplemental_lights_n_or_e_approach)
        self.form_layout_gcws_lights.addRow('S or W Road Approach:', self.input_light_units_observe_supplemental_lights_s_or_w_approach)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Are back light units visible by stopped vehicles at least 15 m?'))
        self.form_layout_gcws_lights.addRow('N or E Road Approach:', self.input_light_units_observe_visibility_back_lights_n_or_e_approach)
        self.form_layout_gcws_lights.addRow('S or W Road Approach:', self.input_light_units_observe_visibility_back_lights_s_or_w_approach)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Are lights installed exclusively for sidewalks, paths or trails visible for at least 30 m?'))
        self.form_layout_gcws_lights.addRow('N or E Rail Approach:', self.input_light_units_observe_sidewalks_n_or_e_approach)
        self.form_layout_gcws_lights.addRow('S or W Rail Approach:', self.input_light_units_observe_sidewalks_s_or_w_approach)
        self.form_layout_gcws_lights.addRow('Are cantilevers as shown in Figure 12-3?', self.input_light_units_observe_cantilevers_per_fig_12_3)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Distance from nearest rail (m):'))
        self.form_layout_gcws_lights.addRow('N or E Rail Approach:', self.input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail)
        self.form_layout_gcws_lights.addRow('S or W Rail Approach:', self.input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Distance from travelled way (m):'))
        self.form_layout_gcws_lights.addRow('N or E Rail Approach:', self.input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road)
        self.form_layout_gcws_lights.addRow('S or W Rail Approach:', self.input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('Height (m):'))
        self.form_layout_gcws_lights.addRow('N or E Rail Approach:', self.input_light_units_measure_cantilevers_n_or_e_approach_height)
        self.form_layout_gcws_lights.addRow('S or W Rail Approach:', self.input_light_units_measure_cantilevers_s_or_w_approach_height)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('DR (m):'))
        self.form_layout_gcws_lights.addRow('N or E Rail Approach:', self.input_light_units_measure_cantilevers_n_or_e_approach_dr)
        self.form_layout_gcws_lights.addRow('S or W Rail Approach:', self.input_light_units_measure_cantilevers_s_or_w_approach_dr)
        self.form_layout_gcws_lights.addRow(qtw.QLabel('DL (m):'))
        self.form_layout_gcws_lights.addRow('N or E Rail Approach:', self.input_light_units_measure_cantilevers_n_or_e_approach_dl)
        self.form_layout_gcws_lights.addRow('S or W Rail Approach:', self.input_light_units_measure_cantilevers_s_or_w_approach_dl)
        self.form_layout_gcws_lights.addRow('Light Unit Comments:', self.input_light_units_comments)

        # layout self.container widgets - GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #TODO self.form_layout_gcws_gates.addRow('Gate arm delay (Recommended) (s):', self.input_gates_gcws_calculate_gate_arm_clearance_time_recommended)
        self.form_layout_gcws_gates.addRow('Gate Arm Delay Time (from Plans) (s):', self.input_gates_gcws_rail_gate_arm_delay_time_design)
        self.form_layout_gcws_gates.addRow('Gate Arm Descent Time (from Plans) (s)', self.input_gates_gcws_rail_gate_arm_descent_time_design)
        #TODO self.form_layout_gcws_gates.addRow('Inner Gate Arm Delay Time for Adjacent Track Interconnected Highway-Rail Grade Crossing (Recommended) (s)', self.input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        self.form_layout_gcws_gates.addRow('nner Gate Arm Delay Time for Adjacent Track Interconnected Highway-Rail Grade Crossing (from Plans) (s)', self.input_gates_gcws_rail_inner_gate_arm_delay_time_design)
        self.form_layout_gcws_gates.addRow('Measure Gate Ascent Time (Actual) (s)', self.input_gates_gcws_measure_gate_ascent_time)
        self.form_layout_gcws_gates.addRow('Measure Gate Descent Time (Actual) (s)', self.input_gates_gcws_measure_gate_descent_time)
        self.form_layout_gcws_gates.addRow('Check Gate Ascent Time (6 to 12 sec)', self.input_gates_gcws_observe_gate_ascent_time)
        self.form_layout_gcws_gates.addRow('Check Gate Descent Time (10 to 15 sec)', self.input_gates_gcws_observe_gate_descent_time)
        self.form_layout_gcws_gates.addRow('Does gate arm come to rest in the horizontal position not less than 5s before the arrival at the crossing of railway equipment?', self.input_gates_gcws_observe_gate_arm_rest)
        self.form_layout_gcws_gates.addRow('Are gates as shown in Figure 12-2?', self.input_gates_gcws_observe_per_fig_12_2)
        self.form_layout_gcws_gates.addRow(qtw.QLabel('Are strips on the gate arm 406 mm (16 in.) wide and aligned vertically?'))
        self.form_layout_gcws_gates.addRow('N or E Road Approach:', self.input_gates_gcws_observe_gate_strips_n_or_e_approach)
        self.form_layout_gcws_gates.addRow('S or W Road Approach:', self.input_gates_gcws_observe_gate_strips_s_or_w_approach)
        self.form_layout_gcws_gates.addRow(qtw.QLabel('Distance between the end of the gate arm and the longitudinal axis of the road approach (m):'))
        self.form_layout_gcws_gates.addRow('N or E Road Approach:', self.input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach)
        self.form_layout_gcws_gates.addRow('S or W Road Approach:', self.input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach)
        self.form_layout_gcws_gates.addRow('Gates for GCWS Comments', self.input_gates_gcws_comments)

        # layout self.container widgets - PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        self.form_layout_aaws.addRow(qtw.QLabel('Are Prepare to Stop at Railway Crossing Sign present?'))
        self.form_layout_aaws.addRow('N or E Road Approach:', self.input_aawd_observe_present_n_or_e_approach)
        self.form_layout_aaws.addRow('S or W Road Approach:', self.input_aawd_observe_present_s_or_w_approach)
        self.form_layout_aaws.addRow(qtw.QLabel('Warrants for a Prepare to Stop at Railway Crossing Sign Per GCR'))
        #TODO self.form_layout_aaws.addRow('A. Is the roadway classified as an expressway?', self.input_aawd_warrant_gcr_lookup_road_classification)
        #TODO self.form_layout_aaws.addRow('B. Is at least one set of front lights on the warning system not clearly visible within the stopping sight distance of at least one of the lanes of the road approach?', self.input_aawd_warrant_gcr_observe_sightline_obstruction)
        #TODO self.form_layout_aaws.addRow('C. Do weather conditions at the grade crossing repeatedly obscure the visibility of the warning system?', self.input_aawd_warrant_gcr_observe_environmental_condition)
        self.form_layout_aaws.addRow(qtw.QLabel('Warrants for a Prepare to Stop at Railway Crossing Sign Per MUTCD'))
        #TODO self.form_layout_aaws.addRow('D. Is the speed limit of the travelled way greater than 90 km/h?', self.input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        #TODO self.form_layout_aaws.addRow('E. Is the crossing at the bottom of a hill or downgrade of considerable length?', self.input_aawd_warrant_mutcd_lookup_significant_road_downgrade)
        self.form_layout_aaws.addRow(qtw.QLabel('Design AAWD Advance Activation Time (s):'))
        #TODO self.form_layout_aaws.addRow('N or E Road Approach:', self.input_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        #TODO self.form_layout_aaws.addRow('S or W Road Approach:', self.input_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        self.form_layout_aaws.addRow(qtw.QLabel('Recommended minimum Advance Warning Flasher Distance from Railway'))
        #TODO self.form_layout_aaws.addRow('N or E Road Approach:', self.input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        #TODO self.form_layout_aaws.addRow('S or W Road Approach:', self.input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        self.form_layout_aaws.addRow(qtw.QLabel('Actual Advance Warning Flasher Distance from Railway'))
        self.form_layout_aaws.addRow('N or E Road Approach:', self.input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual)
        self.form_layout_aaws.addRow('S or W Road Approach:', self.input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual)
        self.form_layout_aaws.addRow(qtw.QLabel('Does the advance activation time provide sufficient time for a vehicle to:'))
        self.form_layout_aaws.addRow(qtw.QLabel('a) clear the grade crossing before the arrival of railway equipment at the crossing surface (FLB)'))
        self.form_layout_aaws.addRow(qtw.QLabel('b) clear the grade crossing before gate arms start to descend (FLBG)'))
        self.form_layout_aaws.addRow('N or E Road Approach:', self.input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach)
        self.form_layout_aaws.addRow('S or W Road Approach:', self.input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach)
        self.form_layout_aaws.addRow('Prepare to Stop at Railway Crossing Sign Comments', self.input_aawd_comments)

        # layout self.container widgets - INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        self.form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Warrants for an Interconnected Traffic Signal'))
        #TODO self.form_layout_interconnection_traffic_signals.addRow('Is there less than 30m between the nearest rail of a grade crossing and the travelled way of an intersection with traffic signals?', self.input_preemption_of_traffic_signals_lookup_proximity_condition)
        #TODO self.form_layout_interconnection_traffic_signals.addRow('Is an Interconnected Traffic Signal required?', self.input_preemption_of_traffic_signals_lookup_required)
        self.form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Other Queuing Condition(s)'))
        self.form_layout_interconnection_traffic_signals.addRow('Is "D" insufficient such that road vehicles might queue onto the rail tracks? (I.E. less than 60 m for traffic signals; 30 m or more for a Stop sign (or 60 m or more for traffic signals) with queued traffic encroaching within 2.4 m of the nearest rail; a situation causing vehicles to routinely queue closer than 2.4 m to the nearest rail in the crossing (Example(s): Yield sign, a roundabout, a pedestrian crossing, a bikeway, or a stopped vehicle waiting to make left turn))', self.input_preemption_of_traffic_signals_observe_queuing_condition)
        #TODO self.form_layout_interconnection_traffic_signals.addRow('Are adjacent traffic signals interconnected with a grade crossing warning system?', self.input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)
        self.form_layout_interconnection_traffic_signals.addRow('Design Preemption activation warning time required for traffic signal preemption (s):', self.input_preemption_of_traffic_signals_road_preemption_warning_time_design)
        self.form_layout_interconnection_traffic_signals.addRow('Actual Preemption activation warning time required for traffic signal preemption (s):', self.input_preemption_of_traffic_signals_road_preemption_warning_time_actual)
        self.form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Field checks:'))
        #TODO self.form_layout_interconnection_traffic_signals.addRow('Date of last pre-emption check?', self.input_preemption_of_traffic_signals_road_date_Last_preemption_check)
        self.form_layout_interconnection_traffic_signals.addRow('Does interconnection provide adequate time to clear traffic from the grade crossing before the arrival of railway equipment?', self.input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate)
        self.form_layout_interconnection_traffic_signals.addRow('Does interconnection prohibit road traffic from moving from the street intersection towards the grade crossing?', self.input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals)
        self.form_layout_interconnection_traffic_signals.addRow('Are there known queuing issues at the tracks?', self.input_preemption_of_traffic_signals_observe_known_queuing_issues)
        self.form_layout_interconnection_traffic_signals.addRow('Are pedestrians accommodated during the pre-emption?', self.input_preemption_of_traffic_signals_observe_pedestrian_accommodation)
        self.form_layout_interconnection_traffic_signals.addRow('Have longer/slower vehicles been considered (compared to Design Vehicle)?', self.input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles)       
        self.form_layout_interconnection_traffic_signals.addRow('Are supplemental signs needed for motorists (no right turn on red light, etc)?', self.input_preemption_of_traffic_signals_observe_supplemental_signage)
        self.form_layout_interconnection_traffic_signals.addRow('Preemption of Traffic Signals Comments', self.input_preemption_of_traffic_signals_comments)

        # layout self.container widgets - WHISTLE CESSATION (GCS SECTION Appendix D)
        self.form_layout_whistle_cessation.addRow('Is train whistling prohibited at this crossing?', self.input_areas_without_train_whistling_rail_anti_whistling_zone)
        self.form_layout_whistle_cessation.addRow('24 hours per day?', self.input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs)
        self.form_layout_whistle_cessation.addRow(qtw.QLabel('Requirements'))
        self.form_layout_whistle_cessation.addRow('Is there evidence of routine unauthorized access (trespassing) on the rail line in the area of the crossing? Comment below.', self.input_areas_without_train_whistling_observe_trespassing_area)
        #TODO self.form_layout_whistle_cessation.addRow('What is the required type of warning system as per Table D-1?', self.input_areas_without_train_whistling_requirements_observe_table_D1)
        #TODO self.form_layout_whistle_cessation.addRow('Further to Column A of Table D-1, is a crossing warning system with gates installed per GCS 9.2?', self.input_areas_without_train_whistling_lookup_gcs_9_2)
        #TODO self.form_layout_whistle_cessation.addRow('Does crossing warning system meet requirements of GCS 12-16?', self.input_areas_without_train_whistling_lookup_gcs_12_to_16)
        #TODO self.form_layout_whistle_cessation.addRow('If Stop and Proceed, is crossing equipped with FLB meeting GCS 12-16 or manually protected?', self.input_areas_without_train_whistling_observe_For_stop_and_proceed)       
        self.form_layout_whistle_cessation.addRow('Whistle Cessation Comments', self.input_areas_without_train_whistling_comments)