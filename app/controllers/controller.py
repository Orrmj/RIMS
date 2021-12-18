from PyQt5.QtCore import QObject, pyqtSlot


class Controller(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # Takes Signal from UI
    
    # INSPECTION DETAILS
    #Group TextBoxes
    #input_inspection_details_assessment_team = None
    
    #Group DatePicker
    #input_inspection_details_date_assessment = None
    
    #Group LineEdits
    #input_inspection_details_crossing_location = None 
    #input_inspection_details_latitude = None 
    #input_inspection_details_location_number = None 
    #input_inspection_details_longitude = None 
    #input_inspection_details_municipality = None 
    #input_inspection_details_road_name = None 
    #input_inspection_details_road_number = None 
    #input_inspection_details_spur_mile = None 
    #input_inspection_details_spur_name = None 
    #input_inspection_details_subdivision_mile = None 

    #Group ComboBoxes
    #input_inspection_details_gcws_type
    @pyqtSlot(str)
    def change_input_inspection_details_gcws_type(self, value):
        self._model.input_inspection_details_gcws_type = value

    #input_inspection_details_grade_crossing_type
    @pyqtSlot(str)
    def change_input_inspection_details_grade_crossing_type(self, value):
        self._model.input_inspection_details_grade_crossing_type = value

    #input_inspection_details_province = None
    #input_inspection_details_railway_authority = None
    #input_inspection_details_reason_for_assessment = None
    #input_inspection_details_road_authority = None
    #input_inspection_details_subdivision_name = None
    #input_inspection_details_track_type = None

    # COLLISION HISTORY (5 YEAR PERIOD)
    #Group TextEdits
    #input_collision_history_comments = None

    #Group LineEdits
    #input_collision_history_fatal_injury 
    @pyqtSlot(int)
    def change_input_collision_history_fatal_injury(self, value):
        self._model.input_collision_history_fatal_injury = value

    #input_collision_history_fatalities = None 
    #input_collision_history_personal_injuries = None
    
    #input_collision_history_personal_injury
    @pyqtSlot(int)
    def change_input_collision_history_personal_injury(self, value):
        self._model.input_collision_history_personal_injury = value

    #input_collision_history_property_damage
    @pyqtSlot(int)
    def change_input_collision_history_property_damage(self, value):
        self._model.input_collision_history_pyqtSlot_damage = value

    #Group Labels
    #TODO input_collision_history_total_5_year_period
    @pyqtSlot(int)
    def input_collision_history_total_5_year_period(self):
        return self.input_collision_history_total_5_year_period

    # GENERAL INFORMATION
    #Group TextEdits
    #input_general_info_comments = None

    #Group LineEdits
    #input_general_info_observe_special_buildings = None 

    #input_general_info_rail_max_railway_operating_speed_freight
    @pyqtSlot(int)
    def change_input_general_info_rail_max_railway_operating_speed_freight(self, value):
        self._model.input_general_info_rail_max_railway_operating_speed_freight = value

    #input_general_info_rail_max_railway_operating_speed_passenger
    @pyqtSlot(int)
    def change_input_general_info_rail_max_railway_operating_speed_passenger(self, value):
        self._model.input_general_info_rail_max_railway_operating_speed_passenger = value

    #input_general_info_rail_no_trains_per_day_freight
    @pyqtSlot(int)
    def change_input_general_info_rail_no_trains_per_day_freight(self, value):
        self._model.input_general_info_rail_no_trains_per_day_freight = value

    #input_general_info_rail_no_trains_per_day_passengers
    @pyqtSlot(int)
    def change_input_general_info_rail_no_trains_per_day_passengers(self, value):
        self._model.input_general_info_rail_no_trains_per_day_passengers = value

    #input_general_info_rail_no_tracks_main
    @pyqtSlot(int)
    def change_input_general_info_rail_no_tracks_main(self, value):
        self._model.input_general_info_rail_no_tracks_main = value

    #input_general_info_rail_no_tracks_other
    @pyqtSlot(int)
    def change_input_general_info_rail_no_tracks_other(self, value):
        self._model.input_general_info_rail_no_tracks_other = value

    #input_general_info_rail_railway_design_speed
    @pyqtSlot(int)
    def change_input_general_info_rail_railway_design_speed(self, value):
        self._model.input_general_info_rail_railway_design_speed = value
 
    #input_general_info_road_aadt_current
    @pyqtSlot(int)
    def change_input_general_info_road_aadt_current(self, value):
        self._model.input_general_info_road_aadt_current = value
 
    #input_general_info_road_aadt_forecast
    @pyqtSlot(int)
    def change_input_general_info_road_aadt_forecast(self, value):
        self._model.input_general_info_road_aadt_forecast = value

    #input_general_info_road_aadt_year_current = None 
    #input_general_info_road_aadt_year_forecasted = None 
    #input_general_info_road_cyclist_per_day = None

    #input_general_info_road_no_traffic_lanes_bidirectional
    @pyqtSlot(int)
    def change_input_general_info_road_no_traffic_lanes_bidirectional(self, value):
        self._model.input_general_info_road_no_traffic_lanes_bidirectional = value

    #input_general_info_road_no_traffic_lanes_northbound_or_eastbound
    @pyqtSlot(int)
    def change_input_general_info_road_no_traffic_lanes_northbound_or_eastbound(self, value):
        self._model.input_general_info_road_no_traffic_lanes_northbound_or_eastbound = value

    #input_general_info_road_no_traffic_lanes_southbound_or_westbound
    @pyqtSlot(int)
    def change_input_general_info_road_no_traffic_lanes_southbound_or_westbound(self, value):
        self._model.input_general_info_road_no_traffic_lanes_southbound_or_westbound = value

    #input_general_info_road_other_users = None 
    #input_general_info_road_other_users_daily_users = None 
    #input_general_info_road_pedestrians_per_day = None 

    #input_general_info_road_speed_design
    @pyqtSlot(int)
    def change_input_general_info_road_speed_design(self, value):
        self._model.input_general_info_road_speed_design = value

    #input_general_info_road_speed_posted = None 

    #Group ComboBoxes
    #input_general_info_observe_roadway_illumination = None
    #input_general_info_observe_surrounding_land_use = None
    #input_general_info_rail_train_switching = None        
    #input_general_info_road_assistive_pedestrian_devices = None

    #input_general_info_road_classification
    @pyqtSlot(list)
    def change_input_general_info_road_classification(self, value):
        self._model.input_general_info_road_classification = value
            
    #input_general_info_road_dangerous_goods_route = None
    #input_general_info_road_school_bus_route = None
    #input_general_info_road_seasonal_volume_fluctuations = None

    #input_general_info_road_sidewalks
    @pyqtSlot(list)
    def change_input_general_info_road_sidewalks(self, value):
        self._model.input_general_info_road_sidewalks = value

    #Group Labels
    #TODO input_general_info_rail_no_tracks_total
    @pyqtSlot(int)
    def change_input_general_info_rail_no_tracks_total(self):
        self.input_general_info_rail_no_tracks_total = None #TODO fix None

    #TODO input_general_info_rail_no_trains_per_day_total
    @pyqtSlot(int)
    def change_input_general_info_rail_no_trains_per_day_total(self):
        return self.input_general_info_rail_no_trains_per_day_total

    #TODO input_general_info_road_no_traffic_lanes_total
    @pyqtSlot(int)
    def input_general_info_road_no_traffic_lanes_total(self):
        return self.input_general_info_road_no_traffic_lanes_total

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Group TextEdits
    #input_design_comments = None

    #Group LineEdits
    #input_design_measure_adjacent_track_clearance_distance
    @pyqtSlot(float)
    def change_input_design_measure_adjacent_track_clearance_distance(self, value):
        self._model.input_design_measure_adjacent_track_clearance_distance = value

    #input_design_measure_adjacent_track_separation_distance
    @pyqtSlot(float)
    def change_input_design_measure_adjacent_track_separation_distance(self, value):
        return self.input_design_measure_adjacent_track_separation_distance

    #input_design_measure_clearance_distance_pedestrian
    @pyqtSlot(float)
    def change_input_design_measure_clearance_distance_pedestrian(self, value):
        self._model.input_design_measure_clearance_distance_pedestrian = value

    #input_design_measure_clearance_distance_vehicle
    @pyqtSlot(float)
    def change_input_design_measure_clearance_distance_vehicle(self, value):
        self._model.input_design_measure_clearance_distance_vehicle = value

    #input_design_road_max_approach_grade_within_s
    @pyqtSlot(float)
    def change_input_design_road_max_approach_grade_within_s(self, value):
        self._model.input_design_road_max_approach_grade_within_s = value

    #Group ComboBoxes
    #input_design_observe_field_acceleration_times_exceed_td = None

    #input_design_road_design_vehicle_type
    @pyqtSlot(list)
    def change_input_design_road_design_vehicle_type(self, value):
        self._model.input_design_road_design_vehicle_type = value

    #Group Labels
    #TODO input_design_calculate_adjacent_track_clearance_time
    @pyqtSlot(float)
    def input_design_calculate_adjacent_track_clearance_time(self):
        return self.input_design_calculate_adjacent_track_clearance_time

    #TODO input_design_calculate_clearance_time_crossing_pedestrian_design_check
    @pyqtSlot(float)
    def input_design_calculate_clearance_time_crossing_pedestrian_design_check(self):
        return self.input_design_calculate_clearance_time_crossing_pedestrian_design_check

    #TODO input_design_calculate_clearance_time_crossing_vehicle_design_check
    @pyqtSlot(float)
    def input_design_calculate_clearance_time_crossing_vehicle_design_check(self):
        return self.input_design_calculate_clearance_time_crossing_vehicle_design_check

    #TODO input_design_calculate_clearance_time_gate_arm_ssd
    @pyqtSlot(float)
    def input_design_calculate_clearance_time_gate_arm_ssd(self):
        return self.input_design_calculate_clearance_time_gate_arm_ssd

    #TODO input_design_calculate_clearance_time_gate_arm_stop
    @pyqtSlot(float)
    def input_design_calculate_clearance_time_gate_arm_stop(self):
        return self.input_design_calculate_clearance_time_gate_arm_stop

    #TODO input_design_calculate_vehicle_travel_distance
    @pyqtSlot(float)
    def input_design_calculate_vehicle_travel_distance(self):
        return self.input_design_calculate_vehicle_travel_distance

    #input_design_input_reaction_time
    @pyqtSlot(int)
    def change_input_design_input_reaction_time(self, value):
        self._model.input_design_input_reaction_time = value

    #TODO input_design_lookup_design_vehicle_class
    @pyqtSlot(str)
    def change_input_design_lookup_design_vehicle_class(self, value):
        self._model.input_design_lookup_design_vehicle_class = value

    #TODO input_design_lookup_design_vehicle_length
    @pyqtSlot(str)
    def input_design_lookup_design_vehicle_length(self, value):
        self._model.input_design_lookup_design_vehicle_length = value

    #TODO input_design_lookup_grade_adjustment_factor
    @pyqtSlot(float)
    def change_input_design_lookup_grade_adjustment_factor(self, value):
        self._model.input_design_lookup_grade_adjustment_factor = value

    #TODO input_design_lookup_vehicle_departure_time_crossing
    @pyqtSlot(float)
    def input_design_lookup_vehicle_departure_time_crossing(self):
        return self.input_design_lookup_vehicle_departure_time_crossing


    #TODO input_design_lookup_vehicle_departure_time_gate_arm_clearance
    @pyqtSlot(float)
    def input_design_lookup_vehicle_departure_time_gate_arm_clearance(self):
        return self.input_design_lookup_vehicle_departure_time_gate_arm_clearance

    # LOCATION OF GRADE CROSSING (GCS SECTION 11)
    #Group TextEdits
    #input_location_of_grade_crossing_comments = None

    #Group LineEdits
    #input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = None 
    #input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = None 
    
    #input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach
    @pyqtSlot(float)
    def change_input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach(self, value):
        self._model.input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = value

    #input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach
    @pyqtSlot(float)
    def change_input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach(self, value):
        self._model.input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = value
  
    #input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach
    @pyqtSlot(float)
    def change_input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach(self, value):
        self._model.input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = value

    #input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach
    @pyqtSlot(float)
    def change_input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach(self, value):
        self._model.input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = value

    #group ComboBoxes
    #input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = None
    #input_location_of_grade_crossing_queue_condition = None
    #input_location_of_grade_crossing_visibility_of_warning_lights = None
    
    # GRADE CROSSING SURFACE (GCS SECTION 5)
    #Group TextEdits
    #input_grade_crossing_surface_comments = None

    #Group LineEdits
    #input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_crossing_surface_width = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = None 
    #input_grade_crossing_surface_measure_flangeway_depth = None 
    #input_grade_crossing_surface_measure_flangeway_width = None 
    #input_grade_crossing_surface_measure_road_surface_median_width = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_side_grinding_depth = None 
    #input_grade_crossing_surface_measure_side_grinding_width = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = None 
    #input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = None 
    #input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = None 

    #Group ComboBoxes
    #input_grade_crossing_surface_observe_crossing_smoothness = None
    #input_grade_crossing_surface_observe_crossing_surface_condition = None
    #input_grade_crossing_surface_observe_material = None
    #input_grade_crossing_surface_observe_road_approach_surface_condition = None
    #input_grade_crossing_surface_observe_road_approach_surface_type = None

    # ROAD GEOMETRY (GCS SECTION 6)
    #Group TextEdits 
    #input_road_geometry_comments = None

    #Group LineEdits
    #input_road_geometry_measure_railway_cross_slope
    @pyqtSlot(float)
    def change_input_road_geometry_measure_railway_cross_slope(self, value):
        self._model.input_road_geometry_measure_railway_cross_slope = value
 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = None 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = None 

    #input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach
    @pyqtSlot(float)
    def change_input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach(self, value):
        self._model.input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = value

    #input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach
    @pyqtSlot(float)
    def change_input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach(self, value):
        self._model.input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = value

    #input_road_geometry_rail_superelevation_n_or_e_approach
    @pyqtSlot(float)
    def change_input_road_geometry_rail_superelevation_n_or_e_approach(self, value):
        self._model.input_road_geometry_rail_superelevation_n_or_e_approach = value

    #input_road_geometry_rail_superelevation_s_or_w_approach
    @pyqtSlot(float)
    def change_input_road_geometry_rail_superelevation_s_or_w_approach(self, value):
        self._model.input_road_geometry_rail_superelevation_s_or_w_approach = value
        
    #input_road_geometry_road_crossing_angle = None 
    
    #input_road_geometry_road_general_approach_grade_n_or_e_approach
    @pyqtSlot(float)
    def change_input_road_geometry_road_general_approach_grade_n_or_e_approach(self, value):
        self._model.input_road_geometry_road_general_approach_grade_n_or_e_approach = value

    #input_road_geometry_road_general_approach_grade_s_or_w_approach
    @pyqtSlot(float)
    def change_input_road_geometry_road_general_approach_grade_s_or_w_approach(self, value):
        self._model.input_road_geometry_road_general_approach_grade_s_or_w_approach = value

    #Group ComboBoxes
    #input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = None
    #input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = None
    #input_road_geometry_observe_low_bed_truck_condition = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = None
    
    #Group Labels
    #TODO input_road_geometry_lookup_gradient_difference
    @pyqtSlot(float)
    def input_road_geometry_lookup_gradient_difference(self):
        return self.input_road_geometry_lookup_gradient_difference
    
    # SIGHTLINES (GCS SECTION 7)
    #Group TextEdits
    #input_sightlines_comments = None
    
    #Group LineEdits
    #input_sightlines_measure_dssd_actual_n_or_e_approach_left = None 
    #input_sightlines_measure_dssd_actual_n_or_e_approach_right = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_left = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_right = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = None 
    #input_sightlines_measure_ssd_actual_n_or_e_approach = None 
    #input_sightlines_measure_ssd_actual_s_or_w_approach = None 

    #Group ComboBoxes
    #input_sightlines_observe_sightline_obstructions = None

    #Group Labels
    #TODO input_sightlines_calculate_dssd_vehicle_min_ft
    @pyqtSlot(float)
    def input_sightlines_calculate_dssd_vehicle_min_ft(self):
        return self.input_sightlines_calculate_dssd_vehicle_min_ft

    #TODO input_sightlines_calculate_dssd_vehicle_min_m
    @pyqtSlot(float)
    def input_sightlines_calculate_dssd_vehicle_min_m(self):
        return self.input_sightlines_calculate_dssd_vehicle_min_m

    #TODO input_sightlines_calculate_dstopped_pedestrian_min_ft
    @pyqtSlot(float)
    def input_sightlines_calculate_dstopped_pedestrian_min_ft(self):
        return self.input_sightlines_calculate_dstopped_pedestrian_min_ft

    #TODO input_sightlines_calculate_dstopped_pedestrian_min_m
    @pyqtSlot(float)
    def input_sightlines_calculate_dstopped_pedestrian_min_m(self):
        return self.input_sightlines_calculate_dstopped_pedestrian_min_m

    #TODO input_sightlines_calculate_dstopped_vehicle_min_ft
    @pyqtSlot(float)
    def input_sightlines_calculate_dstopped_vehicle_min_ft(self):
        return self.input_sightlines_calculate_dstopped_vehicle_min_ft

    #TODO input_sightlines_calculate_dstopped_vehicle_min_m
    @pyqtSlot(float)
    def input_sightlines_calculate_dstopped_vehicle_min_m(self):
        return self.input_sightlines_calculate_dstopped_vehicle_min_m

    #TODO input_sightlines_lookup_ssd_minimum_n_or_e_approach
    @pyqtSlot(float)
    def input_sightlines_lookup_ssd_minimum_n_or_e_approach(self):
        return self.input_sightlines_lookup_ssd_minimum_n_or_e_approach

    #TODO input_sightlines_lookup_ssd_minimum_s_or_w_approach
    @pyqtSlot(float)
    def input_sightlines_lookup_ssd_minimum_s_or_w_approach(self):
        return self.input_sightlines_lookup_ssd_minimum_s_or_w_approach

    # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
    #Group TextEdits
    #DELETE input_signs_and_markings_advisory_speed_comments = None
    #DELETE input_signs_and_markings_comments = None
    #DELETE input_signs_and_markings_emergency_notification_comments = None
    #DELETE input_signs_and_markings_number_of_tracks_comments = None
    #DELETE input_signs_and_markings_railway_crossing_ahead_comments = None
    #DELETE input_signs_and_markings_railway_crossing_comments = None
    #DELETE input_signs_and_markings_stop_comments = None
    #DELETE input_signs_and_markings_stop_sign_ahead_comments = None

    #Group LineEdits
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = None 
    #input_signs_and_markings_stop_n_or_e_approach_height = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_rail = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_road = None 
    #input_signs_and_markings_stop_s_or_w_approach_height = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_rail = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_road = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = None 

    #Group ComboBoxes
    #input_signs_and_markings_advisory_speed_n_or_e_approach_present = None
    #input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_present = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = None
    #input_signs_and_markings_dividing_lines_present = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_condition = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_legible = None
    #input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_present = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_condition = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_legible = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_orientation = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_present = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_present = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_present = None
    #input_signs_and_markings_per_mutcd = None
    #input_signs_and_markings_posted_speed_n_or_e_approach_present = None
    #input_signs_and_markings_posted_speed_s_or_w_approach_present = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_present = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_present = None
    #input_signs_and_markings_sidewalks_present = None
    #input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = None
    #input_signs_and_markings_stop_n_or_e_approach_present = None
    #input_signs_and_markings_stop_n_or_e_approach_same_post = None
    #input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = None
    #input_signs_and_markings_stop_s_or_w_approach_present = None
    #input_signs_and_markings_stop_s_or_w_approach_same_post = None
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = None
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = None

    # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
    # Group Labels
    #TODO input_gcws_warrant_private_9_3
    @pyqtSlot(str)
    def input_gcws_warrant_private_9_3(self):
        return self.input_gcws_warrant_private_9_3

    #TODO input_gcws_warrant_private_9_3_1
    @pyqtSlot(str)
    def input_gcws_warrant_private_9_3_1(self):
        return self.input_gcws_warrant_private_9_3_1

    #TODO input_gcws_warrant_private_9_3_2_a
    @pyqtSlot(str)
    def input_gcws_warrant_private_9_3_2_a(self):
        return self.input_gcws_warrant_private_9_3_2_a

    #TODO input_gcws_warrant_private_9_3_2_b
    @pyqtSlot(str)
    def input_gcws_warrant_private_9_3_2_b(self):
        return self.input_gcws_warrant_private_9_3_2_b

    #TODO input_gcws_warrant_private_9_3_2_c
    @pyqtSlot(str)
    def input_gcws_warrant_private_9_3_2_c(self):
        return self.input_gcws_warrant_private_9_3_2_c

    #TODO input_gcws_warrant_public_9_1
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1(self):
        return self.input_gcws_warrant_public_9_1

    #TODO input_gcws_warrant_public_9_1_a
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1_a(self):
        return self.input_gcws_warrant_public_9_1_a

    #TODO input_gcws_warrant_public_9_1_b
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1_b(self):
        return self.input_gcws_warrant_public_9_1_b

    #TODO input_gcws_warrant_public_9_1_c
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1_c(self):
        return self.input_gcws_warrant_public_9_1_c

    #TODO input_gcws_warrant_public_9_1_d_i
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1_d_i(self):
        return self.input_gcws_warrant_public_9_1_d_i

    #TODO input_gcws_warrant_public_9_1_d_ii
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1_d_ii(self):
        return self.input_gcws_warrant_public_9_1_d_ii

    #TODO input_gcws_warrant_public_9_1_d_iii
    @pyqtSlot(str)
    def input_gcws_warrant_public_9_1_d_iii(self):
        return self.input_gcws_warrant_public_9_1_d_iii

    #TODO input_gcws_warrant_sidewalk_9_5
    @pyqtSlot(str)
    def input_gcws_warrant_sidewalk_9_5(self):
        return self.input_gcws_warrant_sidewalk_9_5

    #TODO input_gates_gcws_warrant_private_9_4_1_a
    @pyqtSlot(str)
    def input_gates_gcws_warrant_private_9_4_1_a(self):
        return self.input_gates_gcws_warrant_private_9_4_1_a

    #TODO input_gates_gcws_warrant_private_9_4_1_b
    @pyqtSlot(str)
    def input_gates_gcws_warrant_private_9_4_1_b(self):
        return self.input_gates_gcws_warrant_private_9_4_1_b

    #TODO input_gates_gcws_warrant_private_9_4_1_c
    @pyqtSlot(str)
    def input_gates_gcws_warrant_private_9_4_1_c(self):
        return self.input_gates_gcws_warrant_private_9_4_1_c

    #TODO input_gates_gcws_warrant_public_9_2_1_a
    @pyqtSlot(str)
    def input_gates_gcws_warrant_public_9_2_1_a(self):
        return self.input_gates_gcws_warrant_public_9_2_1_a

    #TODO input_gates_gcws_warrant_public_9_2_1_b
    @pyqtSlot(str)
    def input_gates_gcws_warrant_public_9_2_1_b(self):
        return self.input_gates_gcws_warrant_public_9_2_1_b

    #TODO input_gates_gcws_warrant_public_9_2_1_c
    @pyqtSlot(str)
    def input_gates_gcws_warrant_public_9_2_1_c(self):
        return self.input_gates_gcws_warrant_public_9_2_1_c

    #TODO input_gates_gcws_warrant_public_9_2_1_d
    @pyqtSlot(str)
    def input_gates_gcws_warrant_public_9_2_1_d(self):
        return self.input_gates_gcws_warrant_public_9_2_1_d

    #TODO input_gates_gcws_warrant_public_9_2_1_e
    @pyqtSlot(str)
    def input_gates_gcws_warrant_public_9_2_1_e(self):
        return self.input_gates_gcws_warrant_public_9_2_1_e

    #TODO input_gates_gcws_warrant_sidewalk_9_6
    @pyqtSlot(str)
    def input_gates_gcws_warrant_sidewalk_9_6(self):
        return self.input_gates_gcws_warrant_sidewalk_9_6

    #input_gcws_warrants_comments = None

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Group TextEdits
    #input_gcws_comments = None
        
    #Group LineEdits
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_road = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = None 
    #input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_road = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = None 
    #input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = None 
    #input_gcws_rail_crossing_warning_time_actual = None 

    #Group ComboBox
    #input_gcws_observe_bell_if_sidewalk = None
    #input_gcws_observe_bells_condition = None
    #input_gcws_observe_bells_n_or_e_approach = None
    #input_gcws_observe_bells_s_or_w_approach = None
    #input_gcws_observe_cantilever_lights_condition = None
    #input_gcws_observe_cantilever_lights_n_or_e_approach = None
    #input_gcws_observe_cantilever_lights_s_or_w_approach = None
    #input_gcws_observe_gates_condition = None
    #input_gcws_observe_gates_n_or_e_approach = None
    #input_gcws_observe_gates_s_or_w_approach = None
    #input_gcws_observe_gcws_limited_use_with_walk_light_assembly = None
    #input_gcws_observe_gcws_limited_use_without_walk_light_assembly = None
    #input_gcws_observe_light_units_condition = None
    #input_gcws_observe_light_units_n_or_e_approach = None
    #input_gcws_observe_light_units_s_or_w_approach = None
    #input_gcws_observe_warning_time_consistency = None   
    #input_gcws_observe_warning_time_consistency_reduced_speed = None
    #input_gcws_rail_cut_out_circuit_requirements = None
    #input_gcws_rail_directional_stick_circuit_requirements = None
    #input_gcws_rail_self_diagnostic = None

    #Group Labels
    #TODO input_gcws_rail_design_approach_warning_time
    @pyqtSlot(float)
    def input_gcws_rail_design_approach_warning_time(self):
        return self.input_gcws_rail_design_approach_warning_time

    #TODO input_gcws_rail_design_warning_time_adjacent_crossing
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_adjacent_crossing(self):
        return self.input_gcws_rail_design_warning_time_adjacent_crossing

    #TODO input_gcws_rail_design_warning_time_clearance_distance
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_clearance_distance(self):
        return self.input_gcws_rail_design_warning_time_clearance_distance

    #TODO input_gcws_rail_design_warning_time_departure_time_pedestrian
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_departure_time_pedestrian(self):
        return self.input_gcws_rail_design_warning_time_departure_time_pedestrian

    #TODO input_gcws_rail_design_warning_time_departure_time_vehicle
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_departure_time_vehicle(self):
        return self.input_gcws_rail_design_warning_time_departure_time_vehicle

    #TODO input_gcws_rail_design_warning_time_gate_arm_clearance
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_gate_arm_clearance(self):
        return self.input_gcws_rail_design_warning_time_gate_arm_clearance

    #TODO input_gcws_rail_design_warning_time_preemption
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_preemption(self):
        return self.input_gcws_rail_design_warning_time_preemption

    #TODO input_gcws_rail_design_warning_time_ssd
    @pyqtSlot(float)
    def input_gcws_rail_design_warning_time_ssd(self):
        return self.input_gcws_rail_design_warning_time_ssd

    # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
    #Group TextEdits
    #input_light_units_comments = None

    #Group LineEdits
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dl = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dr = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_height = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dl = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dr = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_height = None 
    #input_light_units_measure_n_or_e_approach_height = None 
    #input_light_units_measure_s_or_w_approach_height = None 

    #Group ComboBoxes
    #input_light_units_observe_cantilevers_per_fig_12_3 = None
    #input_light_units_observe_per_fig_12_1 = None
    #input_light_units_observe_sidewalks_n_or_e_approach = None
    #input_light_units_observe_sidewalks_s_or_w_approach = None
    #input_light_units_observe_supplemental_lights_n_or_e_approach = None
    #input_light_units_observe_supplemental_lights_s_or_w_approach = None
    #input_light_units_observe_visibility_back_lights_n_or_e_approach = None
    #input_light_units_observe_visibility_back_lights_s_or_w_approach = None
    #input_light_units_observe_visibility_front_lights_n_or_e_approach = None
    #input_light_units_observe_visibility_front_lights_s_or_w_approach = None

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #Group TextEdits
    #input_gates_gcws_comments = None

    #Group LineEdits
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = None 
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = None 
    #input_gates_gcws_measure_gate_ascent_time = None 
    #input_gates_gcws_measure_gate_descent_time = None 
    #input_gates_gcws_rail_gate_arm_delay_time_design = None 

    #input_gates_gcws_rail_gate_arm_descent_time_design
    @pyqtSlot(float)
    def change_input_gates_gcws_rail_gate_arm_descent_time_design(self, value):
        self._model.input_gates_gcws_rail_gate_arm_descent_time_design = value

    #input_gates_gcws_rail_inner_gate_arm_delay_time_design = None 

    #Group Labels
    #TODO input_gates_gcws_calculate_gate_arm_clearance_time_recommended
    @pyqtSlot(float)
    def change_input_gates_gcws_calculate_gate_arm_clearance_time_recommended(self, value):
        self._model.input_gates_gcws_calculate_gate_arm_clearance_time_recommended = value

    #TODO input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended
    @pyqtSlot(float)
    def input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended(self):
        return self.input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended

    #Group ComboBoxes
    #input_gates_gcws_observe_gate_arm_rest = None
    #input_gates_gcws_observe_gate_ascent_time = None
    #input_gates_gcws_observe_gate_descent_time = None
    #input_gates_gcws_observe_gate_strips_n_or_e_approach = None
    #input_gates_gcws_observe_gate_strips_s_or_w_approach = None
    #input_gates_gcws_observe_per_fig_12_2 = None

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #Group Text Edits
    #input_aawd_comments = None

    #Group LineEdits
    #input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = None 
    #input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = None 

    #Group ComboBoxes
    #input_aawd_observe_present_n_or_e_approach = None
    #input_aawd_observe_present_s_or_w_approach = None
    #input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = None
    #input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = None

    #Group Labels
    #TODO input_aawd_calculate_advance_activation_time_design_n_or_e_approach
    @pyqtSlot(float)
    def input_aawd_calculate_advance_activation_time_design_n_or_e_approach(self):
        return self.input_aawd_calculate_advance_activation_time_design_n_or_e_approach

    #TODO input_aawd_calculate_advance_activation_time_design_s_or_w_approach
    @pyqtSlot(float)
    def input_aawd_calculate_advance_activation_time_design_s_or_w_approach(self):
        return self.input_aawd_calculate_advance_activation_time_design_s_or_w_approach

    #TODO input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended
    @pyqtSlot(float)
    def input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended(self):
        return self.input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended

    #TODO input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended
    @pyqtSlot(float)
    def input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended(self):
        return self.input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended

    #TODO input_aawd_warrant_gcr_lookup_road_classification
    @pyqtSlot(str)
    def input_aawd_warrant_gcr_lookup_road_classification(self):
        return self.input_aawd_warrant_gcr_lookup_road_classification

    #TODO input_aawd_warrant_gcr_observe_environmental_condition
    @pyqtSlot(str)
    def input_aawd_warrant_gcr_observe_environmental_condition(self):
        return self.input_aawd_warrant_gcr_observe_environmental_condition

    #TODO input_aawd_warrant_gcr_observe_sightline_obstruction
    @pyqtSlot(str)
    def input_aawd_warrant_gcr_observe_sightline_obstruction(self):
        return self.input_aawd_warrant_gcr_observe_sightline_obstruction

    #TODO input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr
    @pyqtSlot(str)
    def input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr(self):
        return self.input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr

    #TODO input_aawd_warrant_mutcd_lookup_significant_road_downgrade
    @pyqtSlot(str)
    def input_aawd_warrant_mutcd_lookup_significant_road_downgrade(self):
        return self.input_aawd_warrant_mutcd_lookup_significant_road_downgrade

    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #Group TextEdits
    #input_preemption_of_traffic_signals_comments = None

    #Group LineEdits
    #input_preemption_of_traffic_signals_road_preemption_warning_time_actual = None 
    #input_preemption_of_traffic_signals_road_preemption_warning_time_design = None 

    #Group CombBoxes
    #input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = None
    #input_preemption_of_traffic_signals_observe_known_queuing_issues = None
    #input_preemption_of_traffic_signals_observe_pedestrian_accommodation = None
    #input_preemption_of_traffic_signals_observe_queuing_condition = None
    #input_preemption_of_traffic_signals_observe_supplemental_signage = None
    #input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = None
    #input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = None
    #input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = None

    #Group DatePicker
    #input_preemption_of_traffic_signals_road_date_Last_preemption_check = None

    #Group Labels
    #TODO input_preemption_of_traffic_signals_lookup_proximity_condition
    @pyqtSlot(str)
    def input_preemption_of_traffic_signals_lookup_proximity_condition(self):
        return self.input_preemption_of_traffic_signals_lookup_proximity_condition

    #TODO input_preemption_of_traffic_signals_lookup_required
    @pyqtSlot(str)
    def input_preemption_of_traffic_signals_lookup_required(self):
        return self.input_preemption_of_traffic_signals_lookup_required

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group TextEdits
    #input_areas_without_train_whistling_comments = None

    #Group ComboBoxes
    #input_areas_without_train_whistling_observe_for_stop_and_proceed = None
    #input_areas_without_train_whistling_observe_tresNoneing_area = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = None

    #Group Labels
    #TODO input_areas_without_train_whistling_lookup_gcs_12_to_16
    @pyqtSlot(str)
    def input_areas_without_train_whistling_lookup_gcs_12_to_16(self):
        return self.input_areas_without_train_whistling_lookup_gcs_12_to_16

    #TODO input_areas_without_train_whistling_lookup_gcs_9_2
    @pyqtSlot(str)
    def input_areas_without_train_whistling_lookup_gcs_9_2(self):
        return self.input_areas_without_train_whistling_lookup_gcs_9_2

    #TODO input_areas_without_train_whistling_requirements_observe_table_D1
    @pyqtSlot(str)
    def input_areas_without_train_whistling_requirements_observe_table_D1(self):
        return self.input_areas_without_train_whistling_requirements_observe_table_D1