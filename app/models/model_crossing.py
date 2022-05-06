import math

class ModelGradeCrossing:
    def __init__(self, **kwargs):
        # INSPECTION DETAILS
        #Group TextBoxes
        self._inspection_details_assessment_team = kwargs['inspection_details_assessment_team'] if 'inspection_details_assessment_team' in kwargs else None
        
        '''
        #Group DatePicker
        self.datetimeEdit_inspection_details_date_assessment = qtw.QDatetimeEdit(
            self,
            date=datetime.date.today(),
            calendarPopup=True,
            displayFormat='yyyy-MM-dd'
        )
        '''

        #Group LineEdits
        self._inspection_details_crossing_location = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None  
        self._inspection_details_location_number = kwargs['inspection_details_location_number'] if 'inspection_details_location_number' in kwargs else None 
        self._inspection_details_municipality = kwargs['inspection_details_municipality'] if 'inspection_details_municipality' in kwargs else None 
        self._inspection_details_road_name = kwargs['inspection_details_road_name'] if 'inspection_details_road_name' in kwargs else None 
        self._inspection_details_road_number = kwargs['inspection_details_road_number'] if 'inspection_details_road_number' in kwargs else None 
        self._inspection_details_spur_name = kwargs['inspection_details_spur_name'] if 'inspection_details_spur_name' in kwargs else None 

        #Group DoubleSpinBox
        self._inspection_details_latitude = kwargs['inspection_details_latitude'] if 'inspection_details_latitude' in kwargs else None
        self._inspection_details_longitude = kwargs['inspection_details_longitude'] if 'inspection_details_longitude' in kwargs else None
        self._inspection_details_spur_mile = kwargs['inspection_details_spur_mile'] if 'inspection_details_spur_mile' in kwargs else None 
        self._inspection_details_subdivision_mile = kwargs['inspection_details_subdivision_mile'] if 'inspection_details_subdivision_mile' in kwargs else None 
        
        #Group ComboBoxes
        self._inspection_details_gcws_type = kwargs['inspection_details_gcws_type'] if 'inspection_details_gcws_type' in kwargs else None
        self._inspection_details_grade_crossing_type = kwargs['inspection_details_grade_crossing_type'] if 'inspection_details_grade_crossing_type' in kwargs else None
        self._inspection_details_province = kwargs['inspection_details_province'] if 'inspection_details_province' in kwargs else None
        self._inspection_details_railway_authority = kwargs['inspection_details_railway_authority'] if 'inspection_details_railway_authority' in kwargs else None
        self._inspection_details_reason_for_assessment = kwargs['inspection_details_reason_for_assessment'] if 'inspection_details_reason_for_assessment' in kwargs else None
        self._inspection_details_road_authority = kwargs['inspection_details_road_authority'] if 'inspection_details_road_authority' in kwargs else None
        self._inspection_details_subdivision_name = kwargs['inspection_details_subdivision_name'] if 'inspection_details_subdivision_name' in kwargs else None
        self._inspection_details_track_type = kwargs['inspection_details_track_type'] if 'inspection_details_track_type' in kwargs else None
        
        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        self._collision_history_comments = kwargs['collision_history_comments'] if 'collision_history_comments' in kwargs else None

        #Group SpinBox
        self._collision_history_fatal_injury = kwargs['collision_history_fatal_injury'] if 'collision_history_fatal_injury' in kwargs else None
        self._collision_history_fatalities = kwargs['collision_history_fatalities'] if 'collision_history_fatalities' in kwargs else None 
        self._collision_history_personal_injuries = kwargs['collision_history_personal_injuries'] if 'collision_history_personal_injuries' in kwargs else None 
        self._collision_history_personal_injury = kwargs['collision_history_personal_injury'] if 'collision_history_personal_injury' in kwargs else None 
        self._collision_history_property_damage = kwargs['collision_history_property_damage'] if 'collision_history_property_damage' in kwargs else None

        #Group Labels 
        self._collision_history_total_5_year_period = kwargs['collision_history_total_5_year_period'] if 'collision_history_total_5_year_period' in kwargs else 'No Value'
        self._collision_history_risk_index_initial = kwargs['collision_history_risk_index_initial'] if 'collision_history_risk_index_initial' in kwargs else 'No Value'
        self._collision_history_risk_index_final = kwargs['collision_history_risk_index_final'] if 'collision_history_risk_index_final' in kwargs else 'No Value'

        # GENERAL INFORMATION
        #Group TextEdits
        self._general_info_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group LineEdits
        self._general_info_observe_special_buildings = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_other_users = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group SpinBox
        self._general_info_rail_max_railway_operating_speed_freight = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_rail_max_railway_operating_speed_passenger = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_rail_no_tracks_main = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_rail_no_tracks_other = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_rail_no_trains_per_day_freight = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_rail_no_trains_per_day_passengers = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_aadt_current = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_aadt_forecast = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_aadt_year_current = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_aadt_year_forecasted = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_cyclist_per_day = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_no_traffic_lanes_bidirectional = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_no_traffic_lanes_northbound_or_eastbound = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_no_traffic_lanes_southbound_or_westbound = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_other_users_daily_users = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_pedestrians_per_day = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_speed_design = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._general_info_road_speed_posted = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._general_info_observe_roadway_illumination = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_observe_surrounding_land_use = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_rail_train_switching = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_assistive_pedestrian_devices = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_classification = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_dangerous_goods_route = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_school_bus_route = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_seasonal_volume_fluctuations = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._general_info_road_sidewalks = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group Labels
        self._general_info_rail_no_tracks_total = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._general_info_rail_no_trains_per_day_total = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._general_info_rail_railway_design_speed = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._general_info_road_no_traffic_lanes_total = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        self._design_observe_k_factor_other = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._design_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._design_measure_adjacent_track_clearance_distance = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._design_measure_adjacent_track_separation_distance = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._design_measure_clearance_distance_pedestrian = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._design_measure_clearance_distance_pedestrian_gate_arm_stop = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._design_measure_clearance_distance_vehicle = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._design_road_max_approach_grade_within_s = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._design_observe_k_factor_road_surface_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None		
        self._design_observe_k_factor_crossing_surface_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None		
        self._design_observe_k_factor_superelevation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._design_observe_k_factor_crossing_nearby_intersection = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None        
        self._design_observe_k_factor_vehicle_restrictions = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._design_observe_k_factor_pavement_marking_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._design_observe_field_acceleration_times_exceed_td = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._design_road_design_vehicle_type = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group Labels
        self._design_calculate_adjacent_track_clearance_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_clearance_time_pedestrian_design_check = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_clearance_time_vehicle_design_check = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_gate_arm_clearance_time_pedestrian = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_gate_arm_clearance_time_vehicle_ssd = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_gate_arm_clearance_time_vehicle_stop = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_gate_arm_clearance_time_vehicle_recommended = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_vehicle_departure_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_vehicle_departure_time_grade_adjusted = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_vehicle_departure_time_gate_arm_clearance = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        self._design_calculate_vehicle_travel_distance = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_input_reaction_time.setNum(2)
        self._design_lookup_design_vehicle_class = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_lookup_design_vehicle_length = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_lookup_grade_adjustment_factor = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_measure_clearance_distance_gate_arm_ssd = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._design_measure_clearance_distance_gate_arm_stop = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        self._location_of_grade_crossing_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #group ComboBoxes
        self._location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._location_of_grade_crossing_queue_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._location_of_grade_crossing_visibility_of_warning_lights = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        self._grade_crossing_surface_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_crossing_surface_width = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None         
        self._grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None         
        self._grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None        
        self._grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None        
        self._grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None        
        self._grade_crossing_surface_measure_flangeway_depth = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_flangeway_width = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_road_surface_median_width = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_side_grinding_depth = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_side_grinding_width = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._grade_crossing_surface_observe_crossing_smoothness = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._grade_crossing_surface_observe_crossing_surface_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._grade_crossing_surface_observe_material = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._grade_crossing_surface_observe_road_approach_surface_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._grade_crossing_surface_observe_road_approach_surface_type = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        self._road_geometry_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group SpinBox
        self._road_geometry_road_crossing_angle = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group DoubleSpinBox
        self._road_geometry_measure_railway_cross_slope = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None         
        self._road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None        
        self._road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_rail_superelevation_rate = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_road_general_approach_grade_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._road_geometry_road_general_approach_grade_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._road_geometry_observe_low_bed_truck_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._road_geometry_rail_superelevation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group Labels
        self._road_geometry_lookup_gradient_difference = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        #TBD self._road_geometry_observe_gradient_difference_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        #TBD self._road_geometry_observe_gradient_difference_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        self._sightlines_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        
        #Group DoubleSpinBox
        self._sightlines_measure_dssd_actual_n_or_e_approach_left = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dssd_actual_n_or_e_approach_right = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dssd_actual_s_or_w_approach_left = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dssd_actual_s_or_w_approach_right = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_ssd_actual_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._sightlines_measure_ssd_actual_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._sightlines_observe_sightline_obstructions = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group Labels
        self._sightlines_calculate_dssd_vehicle_min_ft = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_calculate_dssd_vehicle_min_m = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_calculate_dstopped_pedestrian_min_ft = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_calculate_dstopped_pedestrian_min_m = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_calculate_dstopped_vehicle_min_ft = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_calculate_dstopped_vehicle_min_m = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_lookup_existing_active_crossing = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_lookup_existing_active_crossing_with_gates = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_lookup_ssd_minimum_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._sightlines_lookup_ssd_minimum_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE self._signs_and_markings_advisory_speed_comments = pass
        #DELETE self._signs_and_markings_comments = pass
        #DELETE self._signs_and_markings_emergency_notification_comments = pass
        #DELETE self._signs_and_markings_number_of_tracks_comments = pass
        #DELETE self._signs_and_markings_railway_crossing_ahead_comments = pass
        #DELETE self._signs_and_markings_railway_crossing_comments = pass
        #DELETE self._signs_and_markings_stop_comments = pass
        #DELETE self._signs_and_markings_stop_sign_ahead_comments = pass

        #Group DoubleSpinBox
        self._signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_n_or_e_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_n_or_e_approach_location_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_n_or_e_approach_location_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_s_or_w_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_s_or_w_approach_location_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_s_or_w_approach_location_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_sign_ahead_n_or_e_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_sign_ahead_s_or_w_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        
        #Group ComboBoxes
        self._signs_and_markings_advisory_speed_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_advisory_speed_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_dividing_lines_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_n_or_e_approach_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_n_or_e_approach_legible = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_n_or_e_approach_orientation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_s_or_w_approach_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_s_or_w_approach_legible = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_s_or_w_approach_orientation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_emergency_notification_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_number_of_tracks_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_number_of_tracks_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_per_mutcd = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_posted_speed_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_posted_speed_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_railway_crossing_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_sidewalks_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_n_or_e_approach_same_post = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_s_or_w_approach_same_post = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_sign_ahead_n_or_e_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._signs_and_markings_stop_sign_ahead_s_or_w_approach_present = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #Group TextEdits
        self._gcws_warrants_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        
        # Group Labels
        self._gcws_warrant_private_9_3 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_private_9_3_1 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_private_9_3_2_a = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_private_9_3_2_b = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_private_9_3_2_c = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1_a = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1_b = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1_c = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1_d_i = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1_d_ii = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_public_9_1_d_iii = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_warrant_sidewalk_9_5 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_private_9_4_1_a = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_private_9_4_1_b = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_private_9_4_1_c = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_public_9_2_1_a = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_public_9_2_1_b = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_public_9_2_1_c = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_public_9_2_1_d = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_public_9_2_1_e = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gates_gcws_warrant_sidewalk_9_6 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        self._gcws_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        
        #Group SpinBox
        self._gcws_rail_design_warning_time_preemption = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._gcws_measure_warning_device_n_or_e_approach_distance_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_n_or_e_approach_distance_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_s_or_w_approach_distance_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_s_or_w_approach_distance_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gcws_rail_crossing_warning_time_actual = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBox
        self._gcws_observe_bell_if_sidewalk = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_bells_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_bells_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_bells_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_cantilever_lights_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_cantilever_lights_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_cantilever_lights_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_gates_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_gates_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_gates_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_gcws_limited_use_with_walk_light_assembly = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_gcws_limited_use_without_walk_light_assembly = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_light_units_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_light_units_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_light_units_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_warning_time_consistency = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_observe_warning_time_consistency_reduced_speed = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_rail_cut_out_circuit_requirements = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_rail_directional_stick_circuit_requirements = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gcws_rail_self_diagnostic = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group Labels
        self._gcws_rail_design_approach_warning_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_ssd = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_adjacent_crossing = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_clearance_distance = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_departure_time_pedestrian = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_departure_time_vehicle = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_gate_arm_clearance = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._gcws_rail_design_warning_time_ssd = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        self._light_units_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_n_or_e_approach_distance_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_n_or_e_approach_dl = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_n_or_e_approach_dr = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_n_or_e_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_s_or_w_approach_distance_from_road = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_s_or_w_approach_dl = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_s_or_w_approach_dr = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_cantilevers_s_or_w_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_n_or_e_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._light_units_measure_s_or_w_approach_height = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._light_units_observe_cantilevers_per_fig_12_3 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_per_fig_12_1 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_sidewalks_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_sidewalks_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_supplemental_lights_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_supplemental_lights_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_visibility_back_lights_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_visibility_back_lights_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_visibility_front_lights_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._light_units_observe_visibility_front_lights_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        self._gates_gcws_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._gates_gcws_measure_gate_ascent_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gates_gcws_measure_gate_descent_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gates_gcws_rail_gate_arm_delay_time_design = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gates_gcws_rail_gate_arm_descent_time_design = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gates_gcws_rail_inner_gate_arm_delay_time_design = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
 
        #Group DoubleSpinBox
        self._gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group Labels
        self._gates_gcws_calculate_inner_gate_arm_delay_time_recommended = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        #Group ComboBoxes
        self._gates_gcws_observe_gate_arm_rest = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gates_gcws_observe_gate_ascent_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gates_gcws_observe_gate_descent_time = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gates_gcws_observe_gate_strips_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gates_gcws_observe_gate_strips_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._gates_gcws_observe_per_fig_12_2 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
 
        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        self._aawd_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DoubleSpinBox
        self._aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group ComboBoxes
        self._aawd_observe_present_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._aawd_observe_present_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._aawd_road_aawd_sufficient_activation_time_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._aawd_road_aawd_sufficient_activation_time_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._aawd_warrant_gcr_observe_environmental_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._aawd_warrant_gcr_observe_sightline_obstruction = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._aawd_warrant_mutcd_lookup_significant_road_downgrade = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group Labels
        self._aawd_calculate_advance_activation_time_design_n_or_e_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._aawd_calculate_advance_activation_time_design_s_or_w_approach = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._aawd_warrant_gcr_lookup_road_classification = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        
        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        self._preemption_of_traffic_signals_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
    
        #Group SpinBox
        self._preemption_of_traffic_signals_road_preemption_warning_time_actual = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 
        self._preemption_of_traffic_signals_road_preemption_warning_time_design = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None 

        #Group CombBoxes
        self._preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_observe_known_queuing_issues = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_observe_pedestrian_accommodation = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_observe_queuing_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_observe_supplemental_signage = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group DatePicker
        #TODO self._preemption_of_traffic_signals_road_date_Last_preemption_check = pass

        #Group Labels
        self._preemption_of_traffic_signals_lookup_proximity_condition = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._preemption_of_traffic_signals_lookup_required = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        self._areas_without_train_whistling_comments = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group ComboBoxes
        self._areas_without_train_whistling_lookup_gcs_12_to_16 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._areas_without_train_whistling_observe_for_stop_and_proceed = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._areas_without_train_whistling_observe_trespassing_area = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._areas_without_train_whistling_rail_anti_whistling_zone = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None
        self._areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else None

        #Group Labels
        self._areas_without_train_whistling_lookup_gcs_9_2 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._areas_without_train_whistling_requirements_lookup_table_d1_criteria = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'
        self._areas_without_train_whistling_requirements_observe_table_D1 = kwargs['inspection_details_crossing_location'] if 'inspection_details_crossing_location' in kwargs else 'No Value'

    #Calculate collision_history_total_5_year_period
    def handle_collision_history_total_5_year_period(self):       
        collision_history_fatal_injury = self.spinBox_collision_history_fatal_injury.value()
        collision_history_personal_injury = self.spinBox_collision_history_personal_injury.value()
        collision_history_property_damage = self.spinBox_collision_history_property_damage.value()
        
        result = sum([collision_history_fatal_injury, collision_history_personal_injury, collision_history_property_damage])
        self.label_collision_history_total_5_year_period.setNum(result)
        return result
    

    #Calculate collision_history_risk_index_initial
    def handle_collision_history_risk_index_initial(self):
        print('handle_collision_history_risk_index_initial')

        general_info_rail_no_tracks_total = self.handle_general_info_rail_no_tracks_total()
        inspection_details_gcws_type = self.comboBox_inspection_details_gcws_type.currentText()
        gcws_observe_gates_n_or_e_approach = self.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.comboBox_gcws_observe_gates_s_or_w_approach.currentText()

        grade_crossing_surface_observe_road_approach_surface_type = self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.currentText()
        general_info_road_classification = self.comboBox_general_info_road_classification.currentText()
 
        c = self.spinBox_general_info_road_aadt_current.value()               # c = annual average number of highway vehicles per day (total both directions)
        t = self.handle_general_info_rail_no_trains_per_day_total() # t = average total train movements per day
        d = self.handle_general_info_rail_no_trains_per_day_total() # d = average number of thru trains per day during daylight
        mt = self.spinBox_general_info_rail_no_tracks_main.value()             # mt = number of main tracks
        ms = self.handle_general_info_rail_railway_design_speed()   # ms = maximum timetable speed, mph
        hl = self.handle_general_info_road_no_traffic_lanes_total() # hl = number of highway lanes
        
        # hp = highway paved, yes = 1.0, no = 2.0
        split_general_info_road_classification = general_info_road_classification.split()

        if not split_general_info_road_classification:
            hp = 'No Value'
        elif split_general_info_road_classification[1] == 'Freeway' and grade_crossing_surface_observe_road_approach_surface_type == 'Asphalt':
            hp = 1.0
        else:
            hp = 2.0

        #ht = highway type factor value
        dict_general_info_road_classification = dict([
            ('Rural Local Undivided', 4),
            ('Rural Collector Undivided', 3),
            ('Rural Collector Divided', 3),
            ('Rural Arterial Undivided', 2),
            ('Rural Arterial Divided', 2),
            ('Rural Freeway Divided', 1),
            ('Urban Local Undivided', 4),
            ('Urban Collector Undivided', 3),
            ('Urban Collector Divided', 3),
            ('Urban Arterial Undivided', 2),
            ('Urban Arterial Divided', 2),
            ('Private Road', 5),
            ('Pedestrian Crossing', 5)
            ])
        if general_info_road_classification == '':
            ht = 'No Value'
        else:
            ht = dict_general_info_road_classification[general_info_road_classification]       

        if inspection_details_gcws_type == '' or general_info_road_classification == '' or grade_crossing_surface_observe_road_approach_surface_type == '' or gcws_observe_gates_n_or_e_approach == '' or gcws_observe_gates_s_or_w_approach == '' or general_info_rail_no_tracks_total == 'No Value' or mt == 'No Value' or c == 0 or t == 'No Value' or d == 'No Value' or ms == 'No Value' or hl == 'No Value' or hp == 'No Value' or ht == 'No Value':            
            result = "No Value"
            self.label_collision_history_risk_index_initial.setText(result)
        elif inspection_details_gcws_type == 'Passive':
            result = round(0.002268 * ((c * t + 0.2)/0.2)**0.3334 * math.exp(0.2094 * mt) * ((d + 0.2)/0.2)**0.1336 * math.exp(-0.616 * (hp - 1)) * math.exp(0.0077 * ms) * math.exp(-0.1000 * (ht - 1)) * 1, 5)
            self.label_collision_history_risk_index_initial.setNum(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach != 'Yes' or gcws_observe_gates_s_or_w_approach != 'Yes') and (gcws_observe_gates_n_or_e_approach != '' or gcws_observe_gates_s_or_w_approach != ''):
            result = round(0.003646 * ((c * t + 0.2)/0.2)**0.2953 * math.exp(0.1088 * mt) * ((d + 0.2)/0.2)**0.047 * 1 * 1 * 1 * math.exp(0.1380 * (hl - 1)), 5)
            self.label_collision_history_risk_index_initial.setNum(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach == 'Yes' or gcws_observe_gates_s_or_w_approach == 'Yes'):
            result = round(0.001088 * ((c * t + 0.2)/0.2)**0.3116 * math.exp(0.2912 * mt) * 1 * 1 * 1 * 1 * math.exp(0.1036 * (hl - 1)) ,5)
            self.label_collision_history_risk_index_initial.setNum(result)
        else:
            result = 'No Value'
            self.label_collision_history_risk_index_initial.setText(result)
        return result
    
    #Calculate collision_history_risk_index_final
    def handle_collision_history_risk_index_final(self):
        collision_history_risk_index_initial = self.handle_collision_history_risk_index_initial()
        collision_history_total_5_year_period = self.handle_collision_history_total_5_year_period()

        if collision_history_risk_index_initial == 'No Value':
            result = 'No Value'
            self.label_collision_history_risk_index_final.setText(result)
        else:
            result = round(
                sum([ 
                (1/sum([0.05,collision_history_risk_index_initial])) * collision_history_risk_index_initial / sum([5, 1 / sum([0.05, collision_history_risk_index_initial])]),
                collision_history_total_5_year_period / sum([5, 1 / sum([0.05, collision_history_risk_index_initial])])
                ]),
                5)
            self.label_collision_history_risk_index_final.setNum(result)
        return result

    #Calculate general_info_rail_no_tracks_total
    def handle_general_info_rail_no_tracks_total(self):      
        general_info_rail_no_tracks_main = self.spinBox_general_info_rail_no_tracks_main.value()
        general_info_rail_no_tracks_other = self.spinBox_general_info_rail_no_tracks_other.value()
        
        result = sum([general_info_rail_no_tracks_main, general_info_rail_no_tracks_other])
        self.label_general_info_rail_no_tracks_total.setNum(result)
        return result

    #Calculate general_info_rail_no_trains_per_day_total
    def handle_general_info_rail_no_trains_per_day_total(self):       
        general_info_rail_no_trains_per_day_freight = self.spinBox_general_info_rail_no_trains_per_day_freight.value()
        general_info_rail_no_trains_per_day_passengers = self.spinBox_general_info_rail_no_trains_per_day_passengers.value()
        
        result = sum([general_info_rail_no_trains_per_day_freight, general_info_rail_no_trains_per_day_passengers])
        self.label_general_info_rail_no_trains_per_day_total.setNum(result)
        return result

    #Calculate general_info_road_no_traffic_lanes_total
    def handle_general_info_road_no_traffic_lanes_total(self):     
        general_info_road_no_traffic_lanes_bidirectional = self.spinBox_general_info_road_no_traffic_lanes_bidirectional.value()
        general_info_road_no_traffic_lanes_northbound_or_eastbound = self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.value()
        general_info_road_no_traffic_lanes_southbound_or_westbound = self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.value()        
        
        result = sum([general_info_road_no_traffic_lanes_bidirectional, general_info_road_no_traffic_lanes_northbound_or_eastbound, general_info_road_no_traffic_lanes_southbound_or_westbound])
        self.label_general_info_road_no_traffic_lanes_total.setNum(result)
        return result

    #Calculate general_info_rail_railway_design_speed
    def handle_general_info_rail_railway_design_speed(self):
        general_info_rail_max_railway_operating_speed_freight = self.spinBox_general_info_rail_max_railway_operating_speed_freight.value()
        general_info_rail_max_railway_operating_speed_passenger = self.spinBox_general_info_rail_max_railway_operating_speed_passenger.value()        
        
        result = max((general_info_rail_max_railway_operating_speed_freight, general_info_rail_max_railway_operating_speed_passenger))
        self.label_general_info_rail_railway_design_speed.setNum(result)
        return result

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Calculate design_calculate_adjacent_track_clearance_time
    def handle_design_calculate_adjacent_track_clearance_time(self):        
        design_measure_adjacent_track_separation_distance = self.doubleSpinBox_design_measure_adjacent_track_separation_distance.value()
        design_measure_adjacent_track_clearance_distance = self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.value()

        if design_measure_adjacent_track_separation_distance<30.0 or design_measure_adjacent_track_separation_distance>60.0:
            result = "N/A"
            self.label_design_calculate_adjacent_track_clearance_time.setText(result)
        elif design_measure_adjacent_track_separation_distance>=30.0 and design_measure_adjacent_track_separation_distance<=60.0:
            result = math.ceil(sum([20.00,max(0.00,design_measure_adjacent_track_clearance_distance-10.668)/3.048]))
            self.label_design_calculate_adjacent_track_clearance_time.setNum(result)
        return result

    #Calculate design_calculate_clearance_time_pedestrian_design_check
    def handle_design_calculate_clearance_time_pedestrian_design_check(self):
        design_measure_clearance_distance_pedestrian = self.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        
        result = math.ceil(design_measure_clearance_distance_pedestrian/1.22)
        self.label_design_calculate_clearance_time_pedestrian_design_check.setNum(result)
        return result

    #Calculate design_calculate_clearance_time_vehicle_design_check
    def handle_design_calculate_clearance_time_vehicle_design_check(self):
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        design_calculate_vehicle_departure_time_grade_adjusted = self.handle_design_calculate_vehicle_departure_time_grade_adjusted()
        
        if design_calculate_vehicle_departure_time_grade_adjusted == 'N/A':
            result = 'N/A'
            self.label_design_calculate_clearance_time_vehicle_design_check.setText(result)
        elif design_calculate_vehicle_departure_time_grade_adjusted == 'No Value':
            result = 'No Value'
            self.label_design_calculate_clearance_time_vehicle_design_check.setText(result)
        else:
            design_input_reaction_time = float(design_input_reaction_time)
            design_calculate_vehicle_departure_time_crossing_grade_adjusted = float(design_calculate_vehicle_departure_time_grade_adjusted)
            result = math.ceil(sum([design_input_reaction_time,design_calculate_vehicle_departure_time_crossing_grade_adjusted]))
            self.label_design_calculate_clearance_time_vehicle_design_check.setNum(result)
        return result

    #TODO
    #Calculate design_calculate_gate_arm_clearance_time_pedestrian
    def handle_design_calculate_gate_arm_clearance_time_pedestrian(self):
        pass

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_ssd
    def handle_design_calculate_gate_arm_clearance_time_vehicle_ssd(self):
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length()
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach()
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach()

        if design_road_design_vehicle_type == "Pedestrian Only":
            result = "N/A"
            self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setText(result)
        elif design_road_design_vehicle_type == '' or design_lookup_design_vehicle_length == "No Value" or sightlines_lookup_ssd_minimum_n_or_e_approach == "No Value" or sightlines_lookup_ssd_minimum_s_or_w_approach == "No Value" or general_info_road_speed_design == 0:
            result = "No Value"
            self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setText(result)
        else:
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            sightlines_lookup_ssd_minimum_n_or_e_approach = float(sightlines_lookup_ssd_minimum_n_or_e_approach)
            sightlines_lookup_ssd_minimum_s_or_w_approach = float(sightlines_lookup_ssd_minimum_s_or_w_approach)
            result = math.ceil(sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), 2.0, design_lookup_design_vehicle_length]) / (0.278 * general_info_road_speed_design))
            self.label_design_calculate_gate_arm_clearance_time_vehicle_ssd.setNum(result)
        return result

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_stop
    def handle_design_calculate_gate_arm_clearance_time_vehicle_stop(self):
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        design_lookup_grade_adjustment_factor = self.handle_design_lookup_grade_adjustment_factor()
        design_calculate_vehicle_departure_time_gate_arm_clearance = self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance()

        if design_calculate_vehicle_departure_time_gate_arm_clearance == 'N/A' or design_lookup_grade_adjustment_factor == 'N/A':
            result = 'N/A'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setText(result)
        elif design_calculate_vehicle_departure_time_gate_arm_clearance == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setText(result)
        else:
            design_input_reaction_time = float(design_input_reaction_time)
            design_calculate_vehicle_departure_time_gate_arm_clearance = float(design_calculate_vehicle_departure_time_gate_arm_clearance)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = math.ceil(sum([design_input_reaction_time, design_calculate_vehicle_departure_time_gate_arm_clearance * design_lookup_grade_adjustment_factor]))
            self.label_design_calculate_gate_arm_clearance_time_vehicle_stop.setNum(result)
        return result

    #Calculate design_calculate_gate_arm_clearance_time_vehicle_recommended
    def handle_design_calculate_gate_arm_clearance_time_vehicle_recommended(self):
        design_calculate_gate_arm_clearance_time_vehicle_ssd = self.handle_design_calculate_gate_arm_clearance_time_vehicle_ssd()
        design_calculate_gate_arm_clearance_time_vehicle_stop = self.handle_design_calculate_gate_arm_clearance_time_vehicle_stop()

        if design_calculate_gate_arm_clearance_time_vehicle_ssd == 'N/A' or design_calculate_gate_arm_clearance_time_vehicle_stop == 'N/A':
            result = 'N/A'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setText(result)
        elif design_calculate_gate_arm_clearance_time_vehicle_ssd == 'No Value' or design_calculate_gate_arm_clearance_time_vehicle_ssd == 'No Value':
            result = 'No Value'
            self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setText(result)
        else:
            design_calculate_clearance_time_gate_arm_ssd = int(design_calculate_gate_arm_clearance_time_vehicle_ssd)
            design_calculate_clearance_time_gate_arm_stop = int(design_calculate_gate_arm_clearance_time_vehicle_ssd)
            result = max(design_calculate_clearance_time_gate_arm_ssd, design_calculate_clearance_time_gate_arm_stop)
            self.label_design_calculate_gate_arm_clearance_time_vehicle_recommended.setNum(result)
        return result

    #Calulcate design_calculate_vehicle_departure_time
    def handle_design_calculate_vehicle_departure_time(self):
        design_measure_clearance_distance_pedestrian = self.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class()
        
        if design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time.setText(result)
        elif design_lookup_design_vehicle_class == 'No Value' or design_calculate_vehicle_travel_distance == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time.setText(result)
        elif design_lookup_design_vehicle_class == 'Cars' and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(4.00,-1.83359063314625E-07 * design_calculate_vehicle_travel_distance**4 + 0.000030862217902978 * design_calculate_vehicle_travel_distance**3 - 0.00243559236227734 * design_calculate_vehicle_travel_distance**2 + 0.194096256511465 * design_calculate_vehicle_travel_distance + 1.9653478726958),4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)
        elif design_lookup_design_vehicle_class == 'Single-Unit Trucks' and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(6.00,2.95895110935529E-06 * design_calculate_vehicle_travel_distance**3 - 0.00120538991988588 * design_calculate_vehicle_travel_distance**2 + 0.23080739982193 * design_calculate_vehicle_travel_distance + 3.11489082547138),4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)
        elif (design_lookup_design_vehicle_class == 'Tractor Trailers' or design_lookup_design_vehicle_class == 'Combination Vehicles' or design_lookup_design_vehicle_class == 'Buses') and design_calculate_vehicle_travel_distance != 'No Value':
            design_calculate_vehicle_travel_distance = float(design_calculate_vehicle_travel_distance)
            result = round(max(7.00,2.43585710133203E-07 * design_calculate_vehicle_travel_distance**4 - 0.0000473118786681759 * design_calculate_vehicle_travel_distance**3 + 0.00169819852156627 * design_calculate_vehicle_travel_distance**2 + 0.211550565362998 * design_calculate_vehicle_travel_distance + 3.96662867415871),4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)        
        elif design_lookup_design_vehicle_class == 'Pedestrian' and design_calculate_vehicle_travel_distance != 'No Value':
            result = round(design_measure_clearance_distance_pedestrian/1.22,4)
            self.label_design_calculate_vehicle_departure_time.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_grade_adjusted
    def handle_design_calculate_vehicle_departure_time_grade_adjusted(self):
        design_calculate_vehicle_departure_time = self.handle_design_calculate_vehicle_departure_time()
        design_lookup_grade_adjustment_factor = self.handle_design_lookup_grade_adjustment_factor()

        if design_calculate_vehicle_departure_time == 'N/A':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        elif design_calculate_vehicle_departure_time == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        else:
            design_lookup_vehicle_departure_time = float(design_calculate_vehicle_departure_time)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = design_lookup_vehicle_departure_time * design_lookup_grade_adjustment_factor
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_gate_arm_clearance
    def handle_design_calculate_vehicle_departure_time_gate_arm_clearance(self):
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class()
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length()

        if design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setText(result)
        elif design_lookup_design_vehicle_class == 'No Value' or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setText(result)
        elif design_lookup_design_vehicle_class == 'Cars' and design_lookup_design_vehicle_length != 'No Value':
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(4.00,-1.83359063314625E-07 * sum([design_lookup_design_vehicle_length,2.00])**4 + 0.000030862217902978 * sum([design_lookup_design_vehicle_length,2.00])**3 - 0.00243559236227073 * sum([design_lookup_design_vehicle_length,2.00])**2 + 0.194096256511465 * sum([design_lookup_design_vehicle_length,2.00]) + 1.9653478726958),4)
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        elif design_lookup_design_vehicle_class == 'Single-Unit Trucks' and design_lookup_design_vehicle_length != 'No Value':            
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(6.00,2.95895110935529E-06 * sum([design_lookup_design_vehicle_length,2.00])**3 - 0.00120538991988588 * sum([design_lookup_design_vehicle_length,2.00])**2 + 0.23080739982193 * sum([design_lookup_design_vehicle_length,2.00]) + 3.11489082547138),4)
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        elif (design_lookup_design_vehicle_class == 'Tractor Trailers' or design_lookup_design_vehicle_class == 'Combination Vehicles' or design_lookup_design_vehicle_class == 'Buses') and design_lookup_design_vehicle_length != 'No Value':
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            result = round(max(7.00,2.43585710133203E-07 * sum([design_lookup_design_vehicle_length,2.00])**4 - 0.0000473118786681759 * sum([design_lookup_design_vehicle_length,2.00])**3 + 0.00169819852156627 * sum([design_lookup_design_vehicle_length,2.00])**2 + 0.211550565362998 * sum([design_lookup_design_vehicle_length,2.00]) + 3.96662867415871),4)
            self.label_design_calculate_vehicle_departure_time_gate_arm_clearance.setNum(result)
        return result

    #Calculate design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted
    def handle_design_calculate_vehicle_departure_time_gate_arm_clearance_grade_adjusted(self):
        design_calculate_vehicle_departure_time_gate_arm_clearance = self.handle_design_calculate_vehicle_departure_time_gate_arm_clearance()
        design_lookup_grade_adjustment_factor = self.handle_design_lookup_grade_adjustment_factor()

        if design_calculate_vehicle_departure_time_gate_arm_clearance == 'N/A':
            result = 'N/A'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        elif design_calculate_vehicle_departure_time_gate_arm_clearance == 'No Value' or design_lookup_grade_adjustment_factor == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setText(result)
        else:
            design_calculate_vehicle_departure_time_gate_arm_clearance = float(design_calculate_vehicle_departure_time_gate_arm_clearance)
            design_lookup_grade_adjustment_factor = float(design_lookup_grade_adjustment_factor)
            result = design_calculate_vehicle_departure_time_gate_arm_clearance * design_lookup_grade_adjustment_factor
            self.label_design_calculate_vehicle_departure_time_grade_adjusted.setNum(result)
        return result

    #Calculate design_calculate_vehicle_travel_distance
    def handle_design_calculate_vehicle_travel_distance(self):
        design_measure_clearance_distance_vehicle = self.doubleSpinBox_design_measure_clearance_distance_vehicle.value()
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length()

        if design_road_design_vehicle_type == 'Pedestrian Only':
            result = 'N/A'
            self.label_design_calculate_vehicle_travel_distance.setText(result)
        elif design_measure_clearance_distance_vehicle == 0.00 or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.label_design_calculate_vehicle_travel_distance.setText(result)
        else:
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)          
            result = sum([design_measure_clearance_distance_vehicle, design_lookup_design_vehicle_length])
            self.label_design_calculate_vehicle_travel_distance.setNum(result)
        return result

    #Calculate design_lookup_design_vehicle_class
    def handle_design_lookup_design_vehicle_class(self):
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        df_table_4_1_general_vehicles = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_1_general_vehicles.csv')

        if design_road_design_vehicle_type == '':
            result = 'No Value'
            self.label_design_lookup_design_vehicle_class.setText(result)
        else:
            result = df_table_4_1_general_vehicles.loc[df_table_4_1_general_vehicles.general_vehicle_descriptions == f'{design_road_design_vehicle_type}','class'].item()
            self.label_design_lookup_design_vehicle_class.setText(result)
        return result

    #Calculate design_lookup_design_vehicle_length
    def handle_design_lookup_design_vehicle_length(self):
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        df_table_4_1_general_vehicles = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_1_general_vehicles.csv')
        
        if design_road_design_vehicle_type == '':
            result = 'No Value'
            self.label_design_lookup_design_vehicle_length.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only':
            result = 0.0
            self.label_design_lookup_design_vehicle_length.setNum(result)
        else:
            result = df_table_4_1_general_vehicles.loc[df_table_4_1_general_vehicles.general_vehicle_descriptions == f'{design_road_design_vehicle_type}','vehicle_length_m'].item()
            self.label_design_lookup_design_vehicle_length.setNum(result)
        return result

    #Calculate design_lookup_grade_adjustment_factor
    def handle_design_lookup_grade_adjustment_factor(self):
        design_road_max_approach_grade_within_s = self.doubleSpinBox_design_road_max_approach_grade_within_s.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class()
        df_table_4_6_ratio_of_acceleration_times_on_road_grades = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_6_ratio_of_acceleration_times_on_road_grades.csv')

        if design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.label_design_lookup_grade_adjustment_factor.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_design_lookup_grade_adjustment_factor.setText(result)
        elif design_road_max_approach_grade_within_s<-3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','-4'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>=-3 and design_road_max_approach_grade_within_s<-1:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','-2'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>=-1 and design_road_max_approach_grade_within_s<=1:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','0'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>1 and design_road_max_approach_grade_within_s<=3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','2'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        elif design_road_max_approach_grade_within_s>3:
            result = df_table_4_6_ratio_of_acceleration_times_on_road_grades.loc[df_table_4_6_ratio_of_acceleration_times_on_road_grades.grade_crossing_design_vehicle == f'{design_lookup_design_vehicle_class}','4'].item()
            self.label_design_lookup_grade_adjustment_factor.setNum(result)
        return result

    # ROAD GEOMETRY (GCS SECTION 6)
    #Calculate road_geometry_lookup_gradient_difference
    def handle_road_geometry_lookup_gradient_difference(self):
        general_info_road_classification = self.comboBox_general_info_road_classification.currentText()
        table_6_1_difference_in_gradient = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_6_1_difference_in_gradient.csv')

        if general_info_road_classification == '':
            result = 'No Value'
            self.label_road_geometry_lookup_gradient_difference.setText(result)
        else:
            result = table_6_1_difference_in_gradient.loc[table_6_1_difference_in_gradient.classification_description == f'{general_info_road_classification}','difference_in_gradient_pct'].item()
            self.label_road_geometry_lookup_gradient_difference.setNum(result)
        return result

    # SIGHTLINES (GCS SECTION 7)
    #Calculate sightlines_lookup_existing_active_crossing
    def handle_sightlines_lookup_existing_active_crossing(self):
        inspection_details_gcws_type = self.comboBox_inspection_details_gcws_type.currentText()

        if inspection_details_gcws_type == '':
            result = 'No Value'
            self.label_sightlines_lookup_existing_active_crossing.setText(result)
        elif inspection_details_gcws_type == 'Active':
            result = 'Yes'
            self.label_sightlines_lookup_existing_active_crossing.setText(result)
        else:
            result = 'No'
            self.label_sightlines_lookup_existing_active_crossing.setText(result)
        return result

    #Calculate sightlines_lookup_existing_active_crossing_with_gates
    def handle_sightlines_lookup_existing_active_crossing_with_gates(self):
        inspection_details_gcws_type = self.comboBox_inspection_details_gcws_type.currentText()
        gcws_observe_gates_n_or_e_approach = self.comboBox_gcws_observe_gates_n_or_e_approach.currentText()
        gcws_observe_gates_s_or_w_approach = self.comboBox_gcws_observe_gates_s_or_w_approach.currentText()

        if inspection_details_gcws_type == '' or (gcws_observe_gates_n_or_e_approach == '' and gcws_observe_gates_s_or_w_approach == ''):
            result = 'No Value'
            self.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        elif inspection_details_gcws_type == 'Active' and (gcws_observe_gates_n_or_e_approach == 'Yes' or gcws_observe_gates_s_or_w_approach == 'Yes'):
            result = 'Yes'
            self.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        else:
            result = 'No'
            self.label_sightlines_lookup_existing_active_crossing_with_gates.setText(result)
        return result

    #Calculate sightlines_calculate_dssd_vehicle_min_ft
    def handle_sightlines_calculate_dssd_vehicle_min_ft(self):
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_measure_clearance_distance_vehicle = self.doubleSpinBox_design_measure_clearance_distance_vehicle.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class()
        design_lookup_design_vehicle_length = self.handle_design_lookup_design_vehicle_length()
        general_info_rail_railway_design_speed = self.handle_general_info_rail_railway_design_speed()
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach()
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach()

        if design_lookup_design_vehicle_class == 'No Value' or general_info_rail_railway_design_speed == 'No Value' or general_info_road_speed_design == 0 or design_measure_clearance_distance_vehicle == 0.0 or sightlines_lookup_ssd_minimum_n_or_e_approach == 'No Value' or sightlines_lookup_ssd_minimum_s_or_w_approach == 'No Value' or design_lookup_design_vehicle_length == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dssd_vehicle_min_ft.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_sightlines_calculate_dssd_vehicle_min_ft.setText(result)
        else:
            design_measure_clearance_distance_vehicle = float(design_measure_clearance_distance_vehicle)
            design_lookup_design_vehicle_length = float(design_lookup_design_vehicle_length)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            general_info_road_speed_design = int(general_info_road_speed_design)
            sightlines_lookup_ssd_minimum_n_or_e_approach = float(sightlines_lookup_ssd_minimum_n_or_e_approach)
            sightlines_lookup_ssd_minimum_s_or_w_approach = float(sightlines_lookup_ssd_minimum_s_or_w_approach)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10,sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), design_measure_clearance_distance_vehicle, design_lookup_design_vehicle_length]) / (0.278* general_info_road_speed_design)), 2)
            self.label_sightlines_calculate_dssd_vehicle_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dssd_vehicle_min_m
    def handle_sightlines_calculate_dssd_vehicle_min_m(self):
        sightlines_calculate_dssd_vehicle_min_ft = self.handle_sightlines_calculate_dssd_vehicle_min_ft()

        if sightlines_calculate_dssd_vehicle_min_ft == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dssd_vehicle_min_m.setText(result)
        elif sightlines_calculate_dssd_vehicle_min_ft == 'N/A':
            result = 'N/A'
            self.label_sightlines_calculate_dssd_vehicle_min_m.setText(result)
        else:
            sightlines_calculate_dssd_vehicle_min_ft = float(sightlines_calculate_dssd_vehicle_min_ft)
            result = sightlines_calculate_dssd_vehicle_min_ft * 0.3048
            self.label_sightlines_calculate_dssd_vehicle_min_m.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_pedestrian_min_ft
    def handle_sightlines_calculate_dstopped_pedestrian_min_ft(self):
        design_calculate_clearance_time_crossing_pedestrian_design_check = self.handle_design_calculate_clearance_time_pedestrian_design_check()
        general_info_rail_railway_design_speed = self.handle_general_info_rail_railway_design_speed()

        if general_info_rail_railway_design_speed == 'No Value' or design_calculate_clearance_time_crossing_pedestrian_design_check == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dstopped_pedestrian_min_ft.setText(result)
        else:
            design_calculate_clearance_time_crossing_pedestrian_design_check = float(design_calculate_clearance_time_crossing_pedestrian_design_check)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10, design_calculate_clearance_time_crossing_pedestrian_design_check),2)
            self.label_sightlines_calculate_dstopped_pedestrian_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_pedestrian_min_m
    def handle_sightlines_calculate_dstopped_pedestrian_min_m(self):
        sightlines_calculate_dstopped_pedestrian_min_ft = self.handle_sightlines_calculate_dstopped_pedestrian_min_ft()

        if sightlines_calculate_dstopped_pedestrian_min_ft == "No Value":
            result = "No Value"
            self.label_sightlines_calculate_dstopped_pedestrian_min_m.setText(result)
        else:
            sightlines_calculate_dstopped_pedestrian_min_ft = float(sightlines_calculate_dstopped_pedestrian_min_ft)
            result = round(sightlines_calculate_dstopped_pedestrian_min_ft * 0.3048, 2)
            self.label_sightlines_calculate_dstopped_pedestrian_min_m.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_vehicle_min_ft
    def handle_sightlines_calculate_dstopped_vehicle_min_ft(self):
        design_calculate_clearance_time_vehicle_design_check = self.handle_design_calculate_clearance_time_vehicle_design_check()
        general_info_rail_railway_design_speed = self.handle_general_info_rail_railway_design_speed()

        if design_calculate_clearance_time_vehicle_design_check == 'N/A':
            result = 'N/A'
            self.label_sightlines_calculate_dstopped_vehicle_min_ft.setText(result)
        elif general_info_rail_railway_design_speed == 'No Value' or design_calculate_clearance_time_vehicle_design_check == 'No Value':
            result = 'No Value'
            self.label_sightlines_calculate_dstopped_vehicle_min_ft.setText(result)
        else:
            design_calculate_clearance_time_crossing_vehicle_design_check = float(design_calculate_clearance_time_vehicle_design_check)
            general_info_rail_railway_design_speed = int(general_info_rail_railway_design_speed)
            result = round(1.47 * general_info_rail_railway_design_speed * max(10, design_calculate_clearance_time_crossing_vehicle_design_check),2)
            self.label_sightlines_calculate_dstopped_vehicle_min_ft.setNum(result)
        return result

    #Calculate sightlines_calculate_dstopped_vehicle_min_m
    def handle_sightlines_calculate_dstopped_vehicle_min_m(self):
        sightlines_calculate_dstopped_vehicle_min_ft = self.handle_sightlines_calculate_dstopped_vehicle_min_ft()

        if sightlines_calculate_dstopped_vehicle_min_ft == 'N/A':
            result = "N/A"
            self.label_sightlines_calculate_dstopped_vehicle_min_m.setText(result)
        elif sightlines_calculate_dstopped_vehicle_min_ft == "No Value":
            result = "No Value"
            self.label_sightlines_calculate_dstopped_vehicle_min_m.setText(result)
        else:
            sightlines_calculate_dstopped_vehicle_min_ft = float(sightlines_calculate_dstopped_vehicle_min_ft)
            result = round(sightlines_calculate_dstopped_vehicle_min_ft * 0.3048, 2)
            self.label_sightlines_calculate_dstopped_vehicle_min_m.setNum(result)
        return result

    #Calculate sightlines_lookup_ssd_minimum_n_or_e_approach
    def handle_sightlines_lookup_ssd_minimum_n_or_e_approach(self):
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class()
        df_table_4_5_SSD_m_passenger_car_class = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_5_SSD_m_passenger_car_class.csv')

        road_geometry_road_general_approach_grade_n_or_e_approach = round(road_geometry_road_general_approach_grade_n_or_e_approach/100.0, 0)

        if road_geometry_road_general_approach_grade_n_or_e_approach >= 0.1:
            road_geometry_road_general_approach_grade_n_or_e_approach = 0.1
        elif road_geometry_road_general_approach_grade_n_or_e_approach <= -0.1:
            road_geometry_road_general_approach_grade_n_or_e_approach = -0.1

        if general_info_road_speed_design == '' or design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setText(result)
        elif general_info_road_speed_design>=0.0 and general_info_road_speed_design<=10:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[0, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=11 and general_info_road_speed_design<=20:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[1, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=21 and general_info_road_speed_design<=30:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[2, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=31 and general_info_road_speed_design<=40:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[3, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=41 and general_info_road_speed_design<=50:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[4, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=51 and general_info_road_speed_design<=60:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[5, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=61 and general_info_road_speed_design<=70:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[6, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=71 and general_info_road_speed_design<=80:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[7, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=81 and general_info_road_speed_design<=90:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[8, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=91 and general_info_road_speed_design<=100:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[9, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        elif general_info_road_speed_design>=101 and general_info_road_speed_design<=110:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[10, [f'{road_geometry_road_general_approach_grade_n_or_e_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(result)
        return result

    #Calculate sightlines_lookup_ssd_minimum_s_or_w_approach
    def handle_sightlines_lookup_ssd_minimum_s_or_w_approach(self):
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_lookup_design_vehicle_class = self.handle_design_lookup_design_vehicle_class()
        df_table_4_5_SSD_m_passenger_car_class = pd.read_csv(r'app\\resources\\data\\TC\\GCS\\table_4_5_SSD_m_passenger_car_class.csv')

        road_geometry_road_general_approach_grade_s_or_w_approach = round(road_geometry_road_general_approach_grade_s_or_w_approach/100.0, 0)

        if road_geometry_road_general_approach_grade_s_or_w_approach >= 0.1:
            road_geometry_road_general_approach_grade_s_or_w_approach = 0.1
        elif road_geometry_road_general_approach_grade_s_or_w_approach <= -0.1:
            road_geometry_road_general_approach_grade_s_or_w_approach = -0.1
    
        if general_info_road_speed_design == '' or design_lookup_design_vehicle_class == 'No Value':
            result = 'No Value'
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setText(result)
        elif design_lookup_design_vehicle_class == 'Pedestrian':
            result = 'N/A'
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setText(result)
        elif general_info_road_speed_design>=0 and general_info_road_speed_design<=10:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[0, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=11 and general_info_road_speed_design<=20:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[1, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=21 and general_info_road_speed_design<=30:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[2, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=31 and general_info_road_speed_design<=40:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[3, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=41 and general_info_road_speed_design<=50:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[4, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=51 and general_info_road_speed_design<=60:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[5, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=61 and general_info_road_speed_design<=70:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[6, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=71 and general_info_road_speed_design<=80:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[7, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=81 and general_info_road_speed_design<=90:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[8, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=91 and general_info_road_speed_design<=100:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[9, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        elif general_info_road_speed_design>=101 and general_info_road_speed_design<=110:
            result = df_table_4_5_SSD_m_passenger_car_class.loc[10, [f'{road_geometry_road_general_approach_grade_s_or_w_approach}']].item()
            self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(result)
        return result

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #self.label_gcws_warrant_private_9_3.valueChanged.connect(self.handle_gcws_warrant_private_9_3)
        #self.label_gcws_warrant_private_9_3_1.valueChanged.connect(self.handle_gcws_warrant_private_9_3_1)
        #self.label_gcws_warrant_private_9_3_2_a.valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_a)
        #self.label_gcws_warrant_private_9_3_2_b.valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_b)
        #self.label_gcws_warrant_private_9_3_2_c.valueChanged.connect(self.handle_gcws_warrant_private_9_3_2_c)
        #self.label_gcws_warrant_public_9_1.valueChanged.connect(self.handle_gcws_warrant_public_9_1)
        #self.label_gcws_warrant_public_9_1_a.valueChanged.connect(self.handle_gcws_warrant_public_9_1_a)
        #self.label_gcws_warrant_public_9_1_b.valueChanged.connect(self.handle_gcws_warrant_public_9_1_b)
        #self.label_gcws_warrant_public_9_1_c.valueChanged.connect(self.handle_gcws_warrant_public_9_1_c)
        #self.label_gcws_warrant_public_9_1_d_i.valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_i)
        #self.label_gcws_warrant_public_9_1_d_ii.valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_ii)
        #self.label_gcws_warrant_public_9_1_d_iii.valueChanged.connect(self.handle_gcws_warrant_public_9_1_d_iii)
        #self.label_gcws_warrant_sidewalk_9_5.valueChanged.connect(self.handle_gcws_warrant_sidewalk_9_5)
        #self.label_gates_gcws_warrant_private_9_4_1_a.valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_a)
        #self.label_gates_gcws_warrant_private_9_4_1_b.valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_b)
        #self.label_gates_gcws_warrant_private_9_4_1_c.valueChanged.connect(self.handle_gates_gcws_warrant_private_9_4_1_c)
        #self.label_gates_gcws_warrant_public_9_2_1_a.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_a)
        #self.label_gates_gcws_warrant_public_9_2_1_b.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_b)
        #self.label_gates_gcws_warrant_public_9_2_1_c.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_c)
        #self.label_gates_gcws_warrant_public_9_2_1_d.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_d)
        #self.label_gates_gcws_warrant_public_9_2_1_e.valueChanged.connect(self.handle_gates_gcws_warrant_public_9_2_1_e)
        #self.label_gates_gcws_warrant_sidewalk_9_6.valueChanged.connect(self.handle_gates_gcws_warrant_sidewalk_9_6)

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Calculate gcws_rail_design_warning_time_clearance_distance
    def handle_gcws_rail_design_warning_time_clearance_distance(self):
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_measure_clearance_distance_pedestrian = self.doubleSpinBox_design_measure_clearance_distance_pedestrian.value()
        design_measure_clearance_distance_vehicle = self.doubleSpinBox_design_measure_clearance_distance_vehicle.value()

        if design_road_design_vehicle_type == '' or (design_measure_clearance_distance_pedestrian == 0.0 and design_measure_clearance_distance_vehicle == 0.0):
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_clearance_distance.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only' and design_measure_clearance_distance_pedestrian != 0.0:
            result = math.ceil(max(20, sum([20, math.ceil(design_measure_clearance_distance_pedestrian - 11.0) / 3.0])))
            self.label_gcws_rail_design_warning_time_clearance_distance.setNum(result)
        else:
            result = math.ceil(max(20, sum([20, math.ceil(design_measure_clearance_distance_vehicle - 11.0) / 3.0])))
            self.label_gcws_rail_design_warning_time_clearance_distance.setNum(result)
        return result
    
    #Calculate gcws_rail_design_warning_time_departure_time_vehicle
    def handle_gcws_rail_design_warning_time_departure_time_vehicle(self):
        design_calculate_clearance_time_vehicle_design_check = self.handle_design_calculate_clearance_time_vehicle_design_check()

        if design_calculate_clearance_time_vehicle_design_check == 'N/A':
            result = 'N/A'
            self.label_gcws_rail_design_warning_time_departure_time_vehicle.setText(result)
        elif design_calculate_clearance_time_vehicle_design_check == 'No Value':
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_departure_time_vehicle.setText(result)
        else:
            design_calculate_clearance_time_crossing_vehicle_design_check = float(design_calculate_clearance_time_vehicle_design_check)
            result = math.ceil(design_calculate_clearance_time_crossing_vehicle_design_check)
            self.label_gcws_rail_design_warning_time_departure_time_vehicle.setNum(result)
        return result

    #Calculate gcws_rail_design_warning_time_departure_time_pedestrian
    def handle_gcws_rail_design_warning_time_departure_time_pedestrian(self):
        design_calculate_clearance_time_crossing_pedestrian_design_check = self.handle_design_calculate_clearance_time_pedestrian_design_check()

        if design_calculate_clearance_time_crossing_pedestrian_design_check == 'No Value':
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_departure_time_pedestrian.setText(result)
        else:
            design_calculate_clearance_time_crossing_pedestrian_design_check = float(design_calculate_clearance_time_crossing_pedestrian_design_check)
            result = math.ceil(design_calculate_clearance_time_crossing_pedestrian_design_check)
            self.label_gcws_rail_design_warning_time_departure_time_pedestrian.setNum(result)
        return result

    #TODO
    #Calculate gcws_rail_design_warning_time_gate_arm_clearance
    def handle_gcws_rail_design_warning_time_gate_arm_clearance(self):
        design_calculate_gate_arm_clearance_time_vehicle_recommended = self.handle_design_calculate_gate_arm_clearance_time_vehicle_recommended()
        gates_gcws_rail_gate_arm_descent_time_design = self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.value()

        if design_calculate_gate_arm_clearance_time_vehicle_recommended == 'No Value' or gates_gcws_rail_gate_arm_descent_time_design == 0.0:
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_gate_arm_clearance.setText(result)
        else:
            result = math.ceil(sum([design_calculate_gate_arm_clearance_time_vehicle_recommended, gates_gcws_rail_gate_arm_descent_time_design, 5.0]))
            self.label_gcws_rail_design_warning_time_gate_arm_clearance.setNum(result)
        return result

    #TODO
    #Calculate gcws_rail_design_warning_time_ssd
    def handle_gcws_rail_design_warning_time_ssd(self):
        sightlines_lookup_ssd_minimum_n_or_e_approach = self.handle_sightlines_lookup_ssd_minimum_n_or_e_approach()
        sightlines_lookup_ssd_minimum_s_or_w_approach = self.handle_sightlines_lookup_ssd_minimum_s_or_w_approach()
        design_road_design_vehicle_type = self.comboBox_design_road_design_vehicle_type.currentText()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance()
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()

        if sightlines_lookup_ssd_minimum_n_or_e_approach == 'No Value' or sightlines_lookup_ssd_minimum_s_or_w_approach == 'No Value' or design_road_design_vehicle_type == '' or design_calculate_vehicle_travel_distance == 'No Value' or general_info_road_speed_design == 0:
            result = 'No Value'
            self.label_gcws_rail_design_warning_time_ssd.setText(result)
        elif design_road_design_vehicle_type == 'Pedestrian Only':
            result = 'N/A'
            self.label_gcws_rail_design_warning_time_ssd.setText(result)
        else:
            result = math.ceil(sum([max(sightlines_lookup_ssd_minimum_n_or_e_approach, sightlines_lookup_ssd_minimum_s_or_w_approach), design_calculate_vehicle_travel_distance]) * 3600 / (general_info_road_speed_design * 10**3))
            self.label_gcws_rail_design_warning_time_ssd.setNum(result)
        return result
    
    #TODO
    #Calculate gcws_rail_design_warning_time_adjacent_crossing
    def handle_gcws_rail_design_warning_time_adjacent_crossing(self):
        pass
    
    #TODO
    #Calculate gcws_rail_design_approach_warning_time
    def handle_gcws_rail_design_approach_warning_time(self):
        pass
        gcws_rail_design_warning_time_preemption = self.spinBox_gcws_rail_design_warning_time_preemption.value()
        gcws_rail_design_warning_time_clearance_distance = self.handle_gcws_rail_design_warning_time_clearance_distance()
        gcws_rail_design_warning_time_departure_time_vehicle = self.handle_gcws_rail_design_warning_time_departure_time_vehicle()
        gcws_rail_design_warning_time_departure_time_pedestrian = self.handle_gcws_rail_design_warning_time_departure_time_pedestrian()
        gcws_rail_design_warning_time_gate_arm_clearance = self.handle_gcws_rail_design_warning_time_gate_arm_clearance() 
        gcws_rail_design_warning_time_ssd = self.handle_gcws_rail_design_warning_time_ssd()

        gcws_rail_design_approach_warning_time = {
            'gcws_rail_design_warning_time_preemption': gcws_rail_design_warning_time_preemption,
            'gcws_rail_design_warning_time_clearance_distance': gcws_rail_design_warning_time_clearance_distance, 
            'gcws_rail_design_warning_time_departure_time_vehicle': gcws_rail_design_warning_time_departure_time_vehicle, 
            'gcws_rail_design_warning_time_departure_time_pedestrian': gcws_rail_design_warning_time_departure_time_pedestrian,
            'gcws_rail_design_warning_time_gate_arm_clearance': gcws_rail_design_warning_time_gate_arm_clearance, 
            'gcws_rail_design_warning_time_ssd': gcws_rail_design_warning_time_ssd
        }
         
        #for i in gcws_rail_design_approach_warning_time:
        #    print (i)

        #return gcws_rail_design_approach_warning_time

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #TODO
    #Calculate gates_gcws_calculate_inner_gate_arm_delay_time_recommended
    def handle_gates_gcws_calculate_inner_gate_arm_delay_time_recommended(self):
        design_calculate_adjacent_track_clearance_time = self.handle_design_calculate_adjacent_track_clearance_time()

        if design_calculate_adjacent_track_clearance_time == 'No Value':
            result = design_calculate_adjacent_track_clearance_time
            self.label_gcws_rail_design_warning_time_ssd.setText(result)
        else:
            result = design_calculate_adjacent_track_clearance_time
            self.label_gcws_rail_design_warning_time_ssd.setNum(result)  
        return result

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #TODO
    #Calculate aawd_calculate_advance_activation_time_design_n_or_e_approach
    def handle_aawd_calculate_advance_activation_time_design_n_or_e_approach(self):
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance()
        aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = self.handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended()

        if general_info_road_speed_design == 0 or design_calculate_vehicle_travel_distance == "No Value" or aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended == "No Value":
            result = "No Value"
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setText(result)
        else:
            result = round(3.6 * sum([design_calculate_vehicle_travel_distance, aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended]) / general_info_road_speed_design, 2)
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_advance_activation_time_design_s_or_w_approach    
    def handle_aawd_calculate_advance_activation_time_design_s_or_w_approach(self):
        general_info_road_speed_design = self.spinBox_general_info_road_speed_design.value()
        design_calculate_vehicle_travel_distance = self.handle_design_calculate_vehicle_travel_distance()
        aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = self.handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended()

        if general_info_road_speed_design == 0 or design_calculate_vehicle_travel_distance == 'No Value' or aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended == 'No Value':
            result = 'No Value'
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setText(result)
        else:
            result = round(3.6 * sum([design_calculate_vehicle_travel_distance, aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended]) / general_info_road_speed_design, 2)
            self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
    def handle_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(self):
        general_info_road_speed_posted = self.spinBox_general_info_road_speed_posted.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        deceleration_rate = 2.6 #typically 2.6m/s2
        gravitational_acceleration = 9.81 #typically 9.81m/s2)

        if general_info_road_speed_posted == 0 or road_geometry_road_general_approach_grade_n_or_e_approach == 0.0 or road_geometry_road_general_approach_grade_s_or_w_approach == 0.0:
            result = 'No Value'
            self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setText(result)
        else:
            result = sum([general_info_road_speed_posted * design_input_reaction_time / 3.6, general_info_road_speed_posted**2 / (25.92 * sum([deceleration_rate, road_geometry_road_general_approach_grade_n_or_e_approach * gravitational_acceleration])) ])
            self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setNum(result)
        return result

    #TODO
    #Calculate aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended
    def handle_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(self):
        general_info_road_speed_posted = self.spinBox_general_info_road_speed_posted.value()
        road_geometry_road_general_approach_grade_n_or_e_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.value()
        road_geometry_road_general_approach_grade_s_or_w_approach = self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.value()
        design_input_reaction_time = self.label_design_input_reaction_time.text()
        deceleration_rate = 2.6 #typically 2.6m/s2
        gravitational_acceleration = 9.81 #typically 9.81m/s2)

        if general_info_road_speed_posted == 0 or road_geometry_road_general_approach_grade_n_or_e_approach == 0.0 or road_geometry_road_general_approach_grade_s_or_w_approach == 0.0:
            result = 'No Value'
            self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setText(result)
        else:
            result = sum([general_info_road_speed_posted * design_input_reaction_time / 3.6, general_info_road_speed_posted**2 / (25.92 * sum([deceleration_rate, road_geometry_road_general_approach_grade_s_or_w_approach * gravitational_acceleration])) ])
            self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setNum(result)
        return result

    #TODO
    #Calculate aawd_warrant_gcr_lookup_road_classification
    def handle_aawd_warrant_gcr_lookup_road_classification(self):
        general_info_road_classification = self.comboBox_general_info_road_classification.currentText()
        general_info_road_classification.split()

        if general_info_road_classification == '':
            result = 'No Value'
            self.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        elif general_info_road_classification[1] == 'Freeway':
            result = 'Yes'
            self.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        else:
            result = 'No'
            self.label_aawd_warrant_gcr_lookup_road_classification.setText(result)
        return result

    #TODO
    #Calculate aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
    def handle_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr(self):
        pass
        #self.spinBox_general_info_road_speed_design
    
    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #TODO
    #Calculate preemption_of_traffic_signals_lookup_proximity_condition
    def preemption_of_traffic_signals_lookup_proximity_condition(self):
        pass
        #self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
        #self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach

    #TODO
    #Calculate preemption_of_traffic_signals_lookup_required
    def preemption_of_traffic_signals_lookup_required(self):
        pass
        #self.label_general_info_rail_railway_design_speed
        #self.label_preemption_of_traffic_signals_lookup_proximity_condition

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group Labels
    #TODO
    #Calculate areas_without_train_whistling_lookup_gcs_9_2
    def handle_areas_without_train_whistling_lookup_gcs_9_2(self):
        pass
        #self.comboBox_gcws_observe_gates_n_or_e_approach
        #self.comboBox_gcws_observe_gates_s_or_w_approach
        #self.label_gates_gcws_warrant_public_9_2_1_a
        #self.label_gates_gcws_warrant_public_9_2_1_b
        #self.label_gates_gcws_warrant_public_9_2_1_c
        #self.label_gates_gcws_warrant_public_9_2_1_d
        #self.label_gates_gcws_warrant_public_9_2_1_e

    #TODO
    #Calculate areas_without_train_whistling_requirements_lookup_table_d1_criteria
    def handle_areas_without_train_whistling_requirements_lookup_table_d1_criteria(self):
        pass
        #self.label_general_info_rail_no_tracks_total
        #self.label_general_info_rail_railway_design_speed

    #TODO
    #Calculate areas_without_train_whistling_requirements_observe_table_D1
    def handle_areas_without_train_whistling_requirements_observe_table_D1(self):
        pass
        #self.comboBox_gcws_observe_gates_n_or_e_approach
        #self.comboBox_gcws_observe_gates_s_or_w_approach
        #self.comboBox_gcws_observe_light_units_n_or_e_approach
        #self.comboBox_gcws_observe_light_units_s_or_w_approach
        #self.label_areas_without_train_whistling_requirements_lookup_table_d1_criteria