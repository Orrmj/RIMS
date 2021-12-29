import sys
import datetime
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from models.model import Model
from controllers.controller import Controller

class ViewCrossingForm(qtw.QWidget):

    submitted = qtc.pyqtSignal([str], [int, str])

    #settings = {'show_warnings': True}
    settings = qtc.QSettings('Michael Orr', 'Crossing App')

    def __init__(self):
        super().__init__()
        self._model = Model()
        self._controller = Controller(self._model)
        self.initializeUI()

        ###################################
        # CONNECT UI-WIDGET TO CONTROLLER #
        ###################################

        # connect ui-widget to controller
        # if ui changes, it sends a signal to an slot on which we connect a controller class.
        # therefore we can receive the signal in the controller
        
        # INSPECTION DETAILS
        #Group TextBoxes
        #input_inspection_details_assessment_team = None
        
        #Group DatePicker
        #input_inspection_details_date_assessment = None
        
        #Group LineEdits
        #input_inspection_details_crossing_location = None 
        #input_inspection_details_location_number = None 
        #input_inspection_details_municipality = None 
        #input_inspection_details_road_name = None 
        #input_inspection_details_road_number = None 
        #input_inspection_details_spur_name = None 

        #Group DoubleSpinBox
        #input_inspection_details_latitude = None 
        #input_inspection_details_longitude = None 
        #input_inspection_details_spur_mile = None 
        #input_inspection_details_subdivision_mile = None

        #Group ComboBoxes
        self.comboBox_inspection_details_gcws_type.activated[str].connect(self._controller.change_input_inspection_details_gcws_type)
        self.comboBox_inspection_details_grade_crossing_type.activated[str].connect(self._controller.change_input_inspection_details_grade_crossing_type)
        #input_inspection_details_province = None
        #input_inspection_details_railway_authority = None
        #input_inspection_details_reason_for_assessment = None
        #input_inspection_details_road_authority = None
        #input_inspection_details_subdivision_name = None
        #input_inspection_details_track_type = None

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        #input_collision_history_comments = None

        #Group SpinBox
        self.spinBox_collision_history_fatal_injury.valueChanged.connect(self._controller.change_input_collision_history_fatal_injury)
        #input_collision_history_fatalities = None 
        #input_collision_history_personal_injuries = None
        self.spinBox_collision_history_personal_injury.valueChanged.connect(self._controller.change_input_collision_history_personal_injury)
        self.spinBox_collision_history_property_damage.valueChanged.connect(self._controller.change_input_collision_history_property_damage)

        #Group Labels
        #self.label_collision_history_total_5_year_period.valueChanged.connect(self._controller.change_input_collision_history_total_5_year_period)
        
        # GENERAL INFORMATION
        #Group TextEdits
        #input_general_info_comments = None

        #Group LineEdits
        #input_general_info_observe_special_buildings = None 
        #input_general_info_road_other_users = None 

        #Group SpinBox
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.valueChanged.connect(self._controller.change_input_general_info_rail_max_railway_operating_speed_freight)     
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.valueChanged.connect(self._controller.change_input_general_info_rail_max_railway_operating_speed_passenger)
        self.spinBox_general_info_rail_no_trains_per_day_freight.valueChanged.connect(self._controller.change_input_general_info_rail_no_trains_per_day_freight)
        self.spinBox_general_info_rail_no_trains_per_day_passengers.valueChanged.connect(self._controller.change_input_general_info_rail_no_trains_per_day_passengers)
        self.spinBox_general_info_rail_no_tracks_main.valueChanged.connect(self._controller.change_input_general_info_rail_no_tracks_main)
        self.spinBox_general_info_rail_no_tracks_other.valueChanged.connect(self._controller.change_input_general_info_rail_no_tracks_other)
        self.spinBox_general_info_rail_railway_design_speed.valueChanged.connect(self._controller.change_input_general_info_rail_railway_design_speed)
        self.spinBox_general_info_road_aadt_current.valueChanged.connect(self._controller.change_input_general_info_road_aadt_current)
        self.spinBox_general_info_road_aadt_forecast.valueChanged.connect(self._controller.change_input_general_info_road_aadt_forecast)
        #input_general_info_road_aadt_year_current = None 
        #input_general_info_road_aadt_year_forecasted = None 
        #input_general_info_road_cyclist_per_day = None
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional.valueChanged.connect(self._controller.change_input_general_info_road_no_traffic_lanes_bidirectional)
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.valueChanged.connect(self._controller.change_input_general_info_road_no_traffic_lanes_northbound_or_eastbound)
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.valueChanged.connect(self._controller.change_input_general_info_road_no_traffic_lanes_southbound_or_westbound)
        #input_general_info_road_other_users_daily_users = None 
        #input_general_info_road_pedestrians_per_day = None 
        self.spinBox_general_info_road_speed_design.valueChanged.connect(self._controller.change_input_general_info_road_speed_design)
        #input_general_info_road_speed_posted = None 

        #Group ComboBoxes
        #input_general_info_observe_roadway_illumination = None
        #input_general_info_observe_surrounding_land_use = None
        #input_general_info_rail_train_switching = None        
        #input_general_info_road_assistive_pedestrian_devices = None
        self.comboBox_general_info_road_classification.activated[str].connect(self._controller.change_input_general_info_road_classification)
        #input_general_info_road_dangerous_goods_route = None
        #input_general_info_road_school_bus_route = None
        #input_general_info_road_seasonal_volume_fluctuations = None
        self.comboBox_general_info_road_sidewalks.activated[str].connect(self._controller.change_input_general_info_road_sidewalks)

        #Group Labels
        #self.label_general_info_rail_no_tracks_total.valueChanged.connect(self._controller.change_input_general_info_rail_no_tracks_total)
        #self.label_general_info_rail_no_trains_per_day_total.valueChanged.connect(self._controller.change_input_general_info_rail_no_trains_per_day_total)
        #self.label_general_info_road_no_traffic_lanes_total.valueChanged.connect(self._controller.change_input_general_info_road_no_traffic_lanes_total)
        
        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        #input_design_comments = None

        #Group DoubleSpinBox
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.valueChanged.connect(self._controller.change_input_design_measure_adjacent_track_clearance_distance)
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance.valueChanged.connect(self._controller.change_input_design_measure_adjacent_track_separation_distance)
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.valueChanged.connect(self._controller.change_input_design_measure_clearance_distance_pedestrian)
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.valueChanged.connect(self._controller.change_input_design_measure_clearance_distance_vehicle)
        self.doubleSpinBox_design_road_max_approach_grade_within_s.valueChanged.connect(self._controller.change_input_design_road_max_approach_grade_within_s)

        #Group ComboBoxes
        #input_design_observe_field_acceleration_times_exceed_td = None
        #TODO self.comboBox_design_road_design_vehicle_type.activated[str].connect(self._controller.change_input_design_road_design_vehicle_type)
        
        #Group Labels
        #self.label_design_calculate_adjacent_track_clearance_time.valueChanged.connect(self._controller.change_input_design_calculate_adjacent_track_clearance_time)
        #self.label_design_calculate_clearance_time_crossing_pedestrian_design_check.valueChanged.connect(self._controller.change_input_design_calculate_clearance_time_crossing_pedestrian_design_check)
        #self.label_design_calculate_clearance_time_crossing_vehicle_design_check.valueChanged.connect(self._controller.change_input_design_calculate_clearance_time_crossing_vehicle_design_check)
        #self.label_design_calculate_clearance_time_gate_arm_ssd.valueChanged.connect(self._controller.change_input_design_calculate_clearance_time_gate_arm_ssd)
        #self.label_design_calculate_clearance_time_gate_arm_stop.valueChanged.connect(self._controller.change_input_design_calculate_clearance_time_gate_arm_stop)
        #self.label_design_calculate_vehicle_travel_distance.valueChanged.connect(self._controller.change_input_design_calculate_vehicle_travel_distance)
        #self.label_design_input_reaction_time.valueChanged.connect(self._controller.change_input_design_input_reaction_time)
        #self.label_design_lookup_design_vehicle_class.valueChanged.connect(self._controller.change_input_design_lookup_design_vehicle_class)
        #self.label_design_lookup_design_vehicle_length.valueChanged.connect(self._controller.change_input_design_lookup_design_vehicle_length)
        #self.label_design_lookup_grade_adjustment_factor.valueChanged.connect(self._controller.change_input_design_lookup_grade_adjustment_factor)
        #self.label_design_lookup_vehicle_departure_time_crossing.valueChanged.connect(self._controller.change_input_design_lookup_vehicle_departure_time_crossing)
        #self.label_design_lookup_vehicle_departure_time_gate_arm_clearance.valueChanged.connect(self._controller.change_input_design_lookup_vehicle_departure_time_gate_arm_clearance)

        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        #input_location_of_grade_crossing_comments = None

        #Group DoubleSpinBox
        #input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = None 
        #input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = None 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.valueChanged.connect(self._controller.change_input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach)
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach.valueChanged.connect(self._controller.change_input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach)
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.valueChanged.connect(self._controller.change_input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach)
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach.valueChanged.connect(self._controller.change_input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach)

        #group ComboBoxes
        #input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = None
        #input_location_of_grade_crossing_queue_condition = None
        #input_location_of_grade_crossing_visibility_of_warning_lights = None
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        #input_grade_crossing_surface_comments = None

        #Group DoubleSpinBox
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

        #Group SpinBox
        #input_road_geometry_road_crossing_angle = None

        #Group DoubleSpinBox
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope.valueChanged.connect(self._controller.change_input_road_geometry_measure_railway_cross_slope)   
        #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = None 
        #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = None 
        #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = None 
        #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = None 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach.valueChanged.connect(self._controller.change_input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach)
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach.valueChanged.connect(self._controller.change_input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach)
        self.doubleSpinBox_road_geometry_rail_superelevation_n_or_e_approach.valueChanged.connect(self._controller.change_input_road_geometry_rail_superelevation_n_or_e_approach)
        self.doubleSpinBox_road_geometry_rail_superelevation_s_or_w_approach.valueChanged.connect(self._controller.change_input_road_geometry_rail_superelevation_s_or_w_approach)
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.valueChanged.connect(self._controller.change_input_road_geometry_road_general_approach_grade_n_or_e_approach)
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.valueChanged.connect(self._controller.change_input_road_geometry_road_general_approach_grade_s_or_w_approach)

        #Group ComboBoxes
        #input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = None
        #input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = None
        #input_road_geometry_observe_low_bed_truck_condition = None
        #input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = None
        #input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = None
        
        #Group Labels
        #self.label_road_geometry_lookup_gradient_difference.valueChanged.connect(self._controller.change_input_road_geometry_lookup_gradient_difference)
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        #input_sightlines_comments = None
        
        #Group DoubleSpinBox
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
        #self.label_sightlines_calculate_dssd_vehicle_min_ft.valueChanged.connect(self._controller.change_input_sightlines_calculate_dssd_vehicle_min_ft)
        #self.label_sightlines_calculate_dssd_vehicle_min_m.valueChanged.connect(self._controller.change_input_sightlines_calculate_dssd_vehicle_min_m)
        #self.label_sightlines_calculate_dstopped_pedestrian_min_ft.valueChanged.connect(self._controller.change_input_sightlines_calculate_dstopped_pedestrian_min_ft)
        #self.label_sightlines_calculate_dstopped_pedestrian_min_m.valueChanged.connect(self._controller.change_input_sightlines_calculate_dstopped_pedestrian_min_m)
        #self.label_sightlines_calculate_dstopped_vehicle_min_ft.valueChanged.connect(self._controller.change_input_sightlines_calculate_dstopped_vehicle_min_ft)
        #self.label_sightlines_calculate_dstopped_vehicle_min_m.valueChanged.connect(self._controller.change_input_sightlines_calculate_dstopped_vehicle_min_m)
        #self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.valueChanged.connect(self._controller.change_input_sightlines_lookup_ssd_minimum_n_or_e_approach)
        #self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.valueChanged.connect(self._controller.change_input_sightlines_lookup_ssd_minimum_s_or_w_approach)

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

        #Group DoubleSpinBox
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
        #Group TextEdits
        #input_gcws_warrants_comments = None

        # Group Labels
        #self.label_gcws_warrant_private_9_3.valueChanged.connect(self._controller.change_input_gcws_warrant_private_9_3)
        #self.label_gcws_warrant_private_9_3_1.valueChanged.connect(self._controller.change_input_gcws_warrant_private_9_3_1)
        #self.label_gcws_warrant_private_9_3_2_a.valueChanged.connect(self._controller.change_input_gcws_warrant_private_9_3_2_a)
        #self.label_gcws_warrant_private_9_3_2_b.valueChanged.connect(self._controller.change_input_gcws_warrant_private_9_3_2_b)
        #self.label_gcws_warrant_private_9_3_2_c.valueChanged.connect(self._controller.change_input_gcws_warrant_private_9_3_2_c)
        #self.label_gcws_warrant_public_9_1.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1)
        #self.label_gcws_warrant_public_9_1_a.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1_a)
        #self.label_gcws_warrant_public_9_1_b.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1_b)
        #self.label_gcws_warrant_public_9_1_c.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1_c)
        #self.label_gcws_warrant_public_9_1_d_i.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1_d_i)
        #self.label_gcws_warrant_public_9_1_d_ii.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1_d_ii)
        #self.label_gcws_warrant_public_9_1_d_iii.valueChanged.connect(self._controller.change_input_gcws_warrant_public_9_1_d_iii)
        #self.label_gcws_warrant_sidewalk_9_5.valueChanged.connect(self._controller.change_input_gcws_warrant_sidewalk_9_5)
        #self.label_gates_gcws_warrant_private_9_4_1_a.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_private_9_4_1_a)
        #self.label_gates_gcws_warrant_private_9_4_1_b.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_private_9_4_1_b)
        #self.label_gates_gcws_warrant_private_9_4_1_c.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_private_9_4_1_c)
        #self.label_gates_gcws_warrant_public_9_2_1_a.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_public_9_2_1_a)
        #self.label_gates_gcws_warrant_public_9_2_1_b.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_public_9_2_1_b)
        #self.label_gates_gcws_warrant_public_9_2_1_c.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_public_9_2_1_c)
        #self.label_gates_gcws_warrant_public_9_2_1_d.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_public_9_2_1_d)
        #self.label_gates_gcws_warrant_public_9_2_1_e.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_public_9_2_1_e)
        #self.label_gates_gcws_warrant_sidewalk_9_6.valueChanged.connect(self._controller.change_input_gates_gcws_warrant_sidewalk_9_6)

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        #input_gcws_comments = None
            
        #Group DoubleSpinBox
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
        #self.label_gcws_rail_design_approach_warning_time.valueChanged.connect(self._controller.change_input_gcws_rail_design_approach_warning_time)
        #self.label_gcws_rail_design_warning_time_adjacent_crossing.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_adjacent_crossing)
        #self.label_gcws_rail_design_warning_time_clearance_distance.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_clearance_distance)
        #self.label_gcws_rail_design_warning_time_departure_time_pedestrian.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_departure_time_pedestrian)
        #self.label_gcws_rail_design_warning_time_departure_time_vehicle.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_departure_time_vehicle)
        #self.label_gcws_rail_design_warning_time_gate_arm_clearance.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_gate_arm_clearance)
        #self.label_gcws_rail_design_warning_time_preemption.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_preemption)
        #self.label_gcws_rail_design_warning_time_ssd.valueChanged.connect(self._controller.change_input_gcws_rail_design_warning_time_ssd)
 
        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        #input_light_units_comments = None

        #Group DoubleSpinBox
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

        #Group DoubleSpinBox
        #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = None 
        #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = None 
        #input_gates_gcws_measure_gate_ascent_time = None 
        #input_gates_gcws_measure_gate_descent_time = None 
        #input_gates_gcws_rail_gate_arm_delay_time_design = None 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.valueChanged.connect(self._controller.change_input_gates_gcws_rail_gate_arm_descent_time_design)
        #input_gates_gcws_rail_inner_gate_arm_delay_time_design = None 

        #Group Labels
        #self.label_gates_gcws_calculate_gate_arm_clearance_time_recommended.valueChanged.connect(self._controller.change_input_gates_gcws_calculate_gate_arm_clearance_time_recommended)
        #self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended.valueChanged.connect(self._controller.change_input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)

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

        #Group DoubleSpinBox
        #input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = None 
        #input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = None 

        #Group ComboBoxes
        #input_aawd_observe_present_n_or_e_approach = None
        #input_aawd_observe_present_s_or_w_approach = None
        #input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = None
        #input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = None

        #Group Labels
        #self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.valueChanged.connect(self._controller.change_input_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        #self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach.valueChanged.connect(self._controller.change_input_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        #self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.valueChanged.connect(self._controller.change_input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        #self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.valueChanged.connect(self._controller.change_input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        #self.label_aawd_warrant_gcr_lookup_road_classification.valueChanged.connect(self._controller.change_input_aawd_warrant_gcr_lookup_road_classification)
        #self.label_aawd_warrant_gcr_observe_environmental_condition.valueChanged.connect(self._controller.change_input_aawd_warrant_gcr_observe_environmental_condition)
        #self.label_aawd_warrant_gcr_observe_sightline_obstruction.valueChanged.connect(self._controller.change_input_aawd_warrant_gcr_observe_sightline_obstruction)
        #self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr.valueChanged.connect(self._controller.change_input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        #self.label_aawd_warrant_mutcd_lookup_significant_road_downgrade.valueChanged.connect(self._controller.change_input_aawd_warrant_mutcd_lookup_significant_road_downgrade)

        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        #input_preemption_of_traffic_signals_comments = None

        #Group DoubleSpinBox
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
        #self.label_preemption_of_traffic_signals_lookup_proximity_condition.valueChanged.connect(self._controller.change_input_preemption_of_traffic_signals_lookup_proximity_condition)
        #self.label_preemption_of_traffic_signals_lookup_required.valueChanged.connect(self._controller.change_input_preemption_of_traffic_signals_lookup_required)

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        #input_areas_without_train_whistling_comments = None

        #Group ComboBoxes
        #input_areas_without_train_whistling_observe_for_stop_and_proceed = None
        #input_areas_without_train_whistling_observe_tresNoneing_area = None
        #input_areas_without_train_whistling_rail_anti_whistling_zone = None
        #input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = None

        #Group Labels
        #self.label_areas_without_train_whistling_lookup_gcs_12_to_16.valueChanged.connect(self._controller.change_input_areas_without_train_whistling_lookup_gcs_12_to_16)
        #self.label_areas_without_train_whistling_lookup_gcs_9_2.valueChanged.connect(self._controller.change_input_areas_without_train_whistling_lookup_gcs_9_2)
        #self.label_areas_without_train_whistling_requirements_observe_table_D1.valueChanged.connect(self._controller.change_input_areas_without_train_whistling_requirements_observe_table_D1)

        ##############################
        # LSITEN MODEL EVENT SIGNALS #
        ##############################
        
        # listen for model event signals
        # connect the method to update the ui to the slots of the model
        # if model sends/emits a signal the ui gets notified
        
        # INSPECTION DETAILS
        #Group TextBoxes
        #input_inspection_details_assessment_team_changed = None
        
        #Group DatePicker
        #input_inspection_details_date_assessment_changed = None
        
        #Group LineEdits
        #input_inspection_details_crossing_location_changed = None 
        #input_inspection_details_latitude_changed = None 
        #input_inspection_details_location_number_changed = None 
        #input_inspection_details_longitude_changed = None 
        #input_inspection_details_municipality_changed = None 
        #input_inspection_details_road_name_changed = None 
        #input_inspection_details_road_number_changed = None 
        #input_inspection_details_spur_mile_changed = None 
        #input_inspection_details_spur_name_changed = None 
        #input_inspection_details_subdivision_mile_changed = None 

        #Group ComboBoxes
        self._model.input_inspection_details_gcws_type_changed.connect(self.on_input_inspection_details_gcws_type_changed)
        self._model.input_inspection_details_grade_crossing_type_changed.connect(self.on_input_inspection_details_grade_crossing_type_changed)
        #input_inspection_details_province_changed = None
        #input_inspection_details_railway_authority_changed = None
        #input_inspection_details_reason_for_assessment_changed = None
        #input_inspection_details_road_authority_changed = None
        #input_inspection_details_subdivision_name_changed = None
        #input_inspection_details_track_type_changed = None

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        #input_collision_history_comments_changed = None

        #Group SpinBox
        self._model.input_collision_history_fatal_injury_changed.connect(self.on_input_collision_history_fatal_injury_changed)
        #input_collision_history_fatalities_changed = None 
        #input_collision_history_personal_injuries_changed = None 
        self._model.input_collision_history_personal_injury_changed.connect(self.on_input_collision_history_personal_injury_changed)
        self._model.input_collision_history_property_damage_changed.connect(self.on_input_collision_history_property_damage_changed)

        #Group Labels
        self._model.input_collision_history_total_5_year_period_changed.connect(self.on_input_collision_history_total_5_year_period_changed)

        # GENERAL INFORMATION
        #Group TextEdits
        #input_general_info_comments_changed = None

        #Group LineEdits
        #input_general_info_observe_special_buildings_changed = None 
        self._model.input_general_info_rail_max_railway_operating_speed_freight_changed.connect(self.on_input_general_info_rail_max_railway_operating_speed_freight_changed)
        self._model.input_general_info_rail_max_railway_operating_speed_passenger_changed.connect(self.on_input_general_info_rail_max_railway_operating_speed_passenger_changed)
        self._model.input_general_info_rail_no_trains_per_day_freight_changed.connect(self.on_input_general_info_rail_no_trains_per_day_freight_changed)  
        self._model.input_general_info_rail_no_trains_per_day_passengers_changed.connect(self.on_input_general_info_rail_no_trains_per_day_passengers_changed)
        self._model.input_general_info_rail_no_tracks_main_changed.connect(self.on_input_general_info_rail_no_tracks_main_changed)
        self._model.input_general_info_rail_no_tracks_other_changed.connect(self.on_input_general_info_rail_no_tracks_other_changed)
        self._model.input_general_info_rail_railway_design_speed_changed.connect(self.on_input_general_info_rail_railway_design_speed_changed)  
        self._model.input_general_info_road_aadt_current_changed.connect(self.on_input_general_info_road_aadt_current_changed)  
        self._model.input_general_info_road_aadt_forecast_changed.connect(self.on_input_general_info_road_aadt_forecast_changed)  
        #input_general_info_road_aadt_year_current_changed = None 
        #input_general_info_road_aadt_year_forecasted_changed = None 
        #input_general_info_road_cyclist_per_day_changed = None 
        self._model.input_general_info_road_no_traffic_lanes_bidirectional_changed.connect(self.on_input_general_info_road_no_traffic_lanes_bidirectional_changed)  
        self._model.input_general_info_road_no_traffic_lanes_northbound_or_eastbound_changed.connect(self.on_input_general_info_road_no_traffic_lanes_northbound_or_eastbound_changed)  
        self._model.input_general_info_road_no_traffic_lanes_southbound_or_westbound_changed.connect(self.on_input_general_info_road_no_traffic_lanes_southbound_or_westbound_changed)  
        #input_general_info_road_other_users_changed = None 
        #input_general_info_road_other_users_daily_users_changed = None 
        #input_general_info_road_pedestrians_per_day_changed = None 
        self._model.input_general_info_road_speed_design_changed.connect(self.on_input_general_info_road_speed_design_changed)  
        #input_general_info_road_speed_posted_changed = None 

        #Group ComboBoxes
        #input_general_info_observe_roadway_illumination_changed = None
        #input_general_info_observe_surrounding_land_use_changed = None
        #input_general_info_rail_train_switching_changed = None        
        #input_general_info_road_assistive_pedestrian_devices_changed = None
        self._model.input_general_info_road_classification_changed.connect(self.on_input_general_info_road_classification_changed)        
        #input_general_info_road_dangerous_goods_route_changed = None
        #input_general_info_road_school_bus_route_changed = None
        #input_general_info_road_seasonal_volume_fluctuations_changed = None
        self._model.input_general_info_road_sidewalks_changed.connect(self.on_input_general_info_road_sidewalks_changed)

        #Group Labels
        self._model.input_general_info_rail_no_tracks_total_changed.connect(self.on_input_general_info_rail_no_tracks_total_changed)
        self._model.input_general_info_rail_no_trains_per_day_total_changed.connect(self.on_input_general_info_rail_no_trains_per_day_total_changed)
        self._model.input_general_info_road_no_traffic_lanes_total_changed.connect(self.on_input_general_info_road_no_traffic_lanes_total_changed)

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        #input_design_comments_changed = None

        #Group DoubleSpinBox
        self._model.input_design_measure_adjacent_track_clearance_distance_changed.connect(self.on_input_design_measure_adjacent_track_clearance_distance_changed)
        self._model.input_design_measure_adjacent_track_separation_distance_changed.connect(self.on_input_design_measure_adjacent_track_separation_distance_changed) 
        self._model.input_design_measure_clearance_distance_pedestrian_changed.connect(self.on_input_design_measure_clearance_distance_pedestrian_changed)
        self._model.input_design_measure_clearance_distance_vehicle_changed.connect(self.on_input_design_measure_clearance_distance_vehicle_changed) 
        self._model.input_design_road_max_approach_grade_within_s_changed.connect(self.on_input_design_road_max_approach_grade_within_s_changed) 

        #Group ComboBoxes
        #input_design_observe_field_acceleration_times_exceed_td = None
        self._model.input_design_road_design_vehicle_type_changed.connect(self.on_input_design_road_design_vehicle_type_changed)

        #Group Labels
        self._model.input_design_calculate_adjacent_track_clearance_time_changed.connect(self.on_input_design_calculate_adjacent_track_clearance_time_changed)
        self._model.input_design_calculate_clearance_time_crossing_pedestrian_design_check_changed.connect(self.on_input_design_calculate_clearance_time_crossing_pedestrian_design_check_changed)
        self._model.input_design_calculate_clearance_time_crossing_vehicle_design_check_changed.connect(self.on_input_design_calculate_clearance_time_crossing_vehicle_design_check_changed)
        self._model.input_design_calculate_clearance_time_gate_arm_ssd_changed.connect(self.on_input_design_calculate_clearance_time_gate_arm_ssd_changed)
        self._model.input_design_calculate_clearance_time_gate_arm_stop_changed.connect(self.on_input_design_calculate_clearance_time_gate_arm_stop_changed)
        self._model.input_design_calculate_vehicle_travel_distance_changed.connect(self.on_input_design_calculate_vehicle_travel_distance_changed)
        self._model.input_design_input_reaction_time_changed.connect(self.on_input_design_input_reaction_time_changed)
        self._model.input_design_lookup_design_vehicle_class_changed.connect(self.on_input_design_lookup_design_vehicle_class_changed)
        self._model.input_design_lookup_design_vehicle_length_changed.connect(self.on_input_design_lookup_design_vehicle_length_changed)
        self._model.input_design_lookup_grade_adjustment_factor_changed.connect(self.on_input_design_lookup_grade_adjustment_factor_changed)
        self._model.input_design_lookup_vehicle_departure_time_crossing_changed.connect(self.on_input_design_lookup_vehicle_departure_time_crossing_changed)
        self._model.input_design_lookup_vehicle_departure_time_gate_arm_clearance_changed.connect(self.on_input_design_lookup_vehicle_departure_time_gate_arm_clearance_changed)
        
        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        #input_location_of_grade_crossing_comments_changed = None

        #Group LineEdits
        #input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach_changed = None 
        #input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach_changed = None 
        self._model.input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach_changed.connect(self.on_input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach_changed) 
        self._model.input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach_changed.connect(self.on_input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach_changed)  
        self._model.input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach_changed.connect(self.on_input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach_changed)  
        self._model.input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach_changed.connect(self.on_input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach_changed)  

        #group ComboBoxes
        #input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk_changed = None
        #input_location_of_grade_crossing_queue_condition_changed = None
        #input_location_of_grade_crossing_visibility_of_warning_lights_changed = None
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        #input_grade_crossing_surface_comments_changed = None

        #Group LineEdits
        #input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach_changed = None 
        #input_grade_crossing_surface_measure_crossing_surface_width_changed = None 
        #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach_changed = None 
        #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach_changed = None 
        #input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface_changed = None 
        #input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface_changed = None 
        #input_grade_crossing_surface_measure_flangeway_depth_changed = None 
        #input_grade_crossing_surface_measure_flangeway_width_changed = None 
        #input_grade_crossing_surface_measure_road_surface_median_width_changed = None 
        #input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach_changed = None 
        #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach_changed = None 
        #input_grade_crossing_surface_measure_side_grinding_depth_changed = None 
        #input_grade_crossing_surface_measure_side_grinding_width_changed = None 
        #input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach_changed = None 
        #input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach_changed = None 
        #input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach_changed = None 

        #Group ComboBoxes
        #input_grade_crossing_surface_observe_crossing_smoothness_changed = None
        #input_grade_crossing_surface_observe_crossing_surface_condition_changed = None
        #input_grade_crossing_surface_observe_material_changed = None
        #input_grade_crossing_surface_observe_road_approach_surface_condition_changed = None
        #input_grade_crossing_surface_observe_road_approach_surface_type_changed = None

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        #input_road_geometry_comments_changed = None

        #Group LineEdits
        self._model.input_road_geometry_measure_railway_cross_slope_changed.connect(self.on_input_road_geometry_measure_railway_cross_slope_changed) 
        #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach_changed = None 
        #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach_changed = None 
        #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach_changed = None 
        #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach_changed = None 
        self._model.input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach_changed.connect(self.on_input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach_changed)
        self._model.input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach_changed.connect(self.on_input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach_changed)
        self._model.input_road_geometry_rail_superelevation_n_or_e_approach_changed.connect(self.on_input_road_geometry_rail_superelevation_n_or_e_approach_changed) 
        self._model.input_road_geometry_rail_superelevation_s_or_w_approach_changed.connect(self.on_input_road_geometry_rail_superelevation_s_or_w_approach_changed) 
        #input_road_geometry_road_crossing_angle_changed = None 
        self._model.input_road_geometry_road_general_approach_grade_n_or_e_approach_changed.connect(self.on_input_road_geometry_road_general_approach_grade_n_or_e_approach_changed)  
        self._model.input_road_geometry_road_general_approach_grade_s_or_w_approach_changed.connect(self.on_input_road_geometry_road_general_approach_grade_s_or_w_approach_changed) 

        #Group ComboBoxes
        #input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach_changed = None
        #input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach_changed = None
        #input_road_geometry_observe_low_bed_truck_condition_changed = None
        #input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach_changed = None
        #input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach_changed = None
        
        #Group Labels
        self._model.input_road_geometry_lookup_gradient_difference_changed.connect(self.on_input_road_geometry_lookup_gradient_difference_changed)
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        #input_sightlines_comments_changed = None
        
        #Group LineEdits
        #input_sightlines_measure_dssd_actual_n_or_e_approach_left_changed = None 
        #input_sightlines_measure_dssd_actual_n_or_e_approach_right_changed = None 
        #input_sightlines_measure_dssd_actual_s_or_w_approach_left_changed = None 
        #input_sightlines_measure_dssd_actual_s_or_w_approach_right_changed = None 
        #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left_changed = None 
        #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right_changed = None 
        #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left_changed = None 
        #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right_changed = None 
        #input_sightlines_measure_ssd_actual_n_or_e_approach_changed = None 
        #input_sightlines_measure_ssd_actual_s_or_w_approach_changed = None 

        #Group ComboBoxes
        #input_sightlines_observe_sightline_obstructions_changed = None

        #Group Labels
        self._model.input_sightlines_calculate_dssd_vehicle_min_ft_changed.connect(self.on_input_sightlines_calculate_dssd_vehicle_min_ft_changed)
        self._model.input_sightlines_calculate_dssd_vehicle_min_m_changed.connect(self.on_input_sightlines_calculate_dssd_vehicle_min_m_changed)
        self._model.input_sightlines_calculate_dstopped_pedestrian_min_ft_changed.connect(self.on_input_sightlines_calculate_dstopped_pedestrian_min_ft_changed)
        self._model.input_sightlines_calculate_dstopped_pedestrian_min_m_changed.connect(self.on_input_sightlines_calculate_dstopped_pedestrian_min_m_changed)
        self._model.input_sightlines_calculate_dstopped_vehicle_min_ft_changed.connect(self.on_input_sightlines_calculate_dstopped_vehicle_min_ft_changed)
        self._model.input_sightlines_calculate_dstopped_vehicle_min_m_changed.connect(self.on_input_sightlines_calculate_dstopped_vehicle_min_m_changed)
        self._model.input_sightlines_lookup_ssd_minimum_n_or_e_approach_changed.connect(self.on_input_sightlines_lookup_ssd_minimum_n_or_e_approach_changed)
        self._model.input_sightlines_lookup_ssd_minimum_s_or_w_approach_changed.connect(self.on_input_sightlines_lookup_ssd_minimum_s_or_w_approach_changed)

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE input_signs_and_markings_advisory_speed_comments_changed = None
        #DELETE input_signs_and_markings_comments_changed = None
        #DELETE input_signs_and_markings_emergency_notification_comments_changed = None
        #DELETE input_signs_and_markings_number_of_tracks_comments_changed = None
        #DELETE input_signs_and_markings_railway_crossing_ahead_comments_changed = None
        #DELETE input_signs_and_markings_railway_crossing_comments_changed = None
        #DELETE input_signs_and_markings_stop_comments_changed = None
        #DELETE input_signs_and_markings_stop_sign_ahead_comments_changed = None

        #Group LineEdits
        #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail_changed = None 
        #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road_changed = None 
        #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height_changed = None 
        #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail_changed = None 
        #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road_changed = None 
        #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height_changed = None 
        #input_signs_and_markings_stop_n_or_e_approach_height_changed = None 
        #input_signs_and_markings_stop_n_or_e_approach_location_from_rail_changed = None 
        #input_signs_and_markings_stop_n_or_e_approach_location_from_road_changed = None 
        #input_signs_and_markings_stop_s_or_w_approach_height_changed = None 
        #input_signs_and_markings_stop_s_or_w_approach_location_from_rail_changed = None 
        #input_signs_and_markings_stop_s_or_w_approach_location_from_road_changed = None 
        #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height_changed = None 
        #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail_changed = None 
        #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road_changed = None 
        #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height_changed = None 
        #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail_changed = None 
        #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road_changed = None 

        #Group ComboBoxes
        #input_signs_and_markings_advisory_speed_n_or_e_approach_present_changed = None
        #input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20_changed = None
        #input_signs_and_markings_advisory_speed_s_or_w_approach_present_changed = None
        #input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20_changed = None
        #input_signs_and_markings_dividing_lines_present_changed = None
        #input_signs_and_markings_emergency_notification_n_or_e_approach_condition_changed = None
        #input_signs_and_markings_emergency_notification_n_or_e_approach_legible_changed = None
        #input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation_changed = None
        #input_signs_and_markings_emergency_notification_n_or_e_approach_present_changed = None
        #input_signs_and_markings_emergency_notification_s_or_w_approach_condition_changed = None
        #input_signs_and_markings_emergency_notification_s_or_w_approach_legible_changed = None
        #input_signs_and_markings_emergency_notification_s_or_w_approach_orientation_changed = None
        #input_signs_and_markings_emergency_notification_s_or_w_approach_present_changed = None
        #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b_changed = None
        #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c_changed = None
        #input_signs_and_markings_number_of_tracks_n_or_e_approach_present_changed = None
        #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b_changed = None
        #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c_changed = None
        #input_signs_and_markings_number_of_tracks_s_or_w_approach_present_changed = None
        #input_signs_and_markings_per_mutcd_changed = None
        #input_signs_and_markings_posted_speed_n_or_e_approach_present_changed = None
        #input_signs_and_markings_posted_speed_s_or_w_approach_present_changed = None
        #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation_changed = None
        #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present_changed = None
        #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation_changed = None
        #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present_changed = None
        #input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a_changed = None
        #input_signs_and_markings_railway_crossing_n_or_e_approach_present_changed = None
        #input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a_changed = None
        #input_signs_and_markings_railway_crossing_s_or_w_approach_present_changed = None
        #input_signs_and_markings_sidewalks_present_changed = None
        #input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4_changed = None
        #input_signs_and_markings_stop_n_or_e_approach_present_changed = None
        #input_signs_and_markings_stop_n_or_e_approach_same_post_changed = None
        #input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4_changed = None
        #input_signs_and_markings_stop_s_or_w_approach_present_changed = None
        #input_signs_and_markings_stop_s_or_w_approach_same_post_changed = None
        #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present_changed = None
        #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present_changed = None

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        # Group Labels
        self._model.input_gcws_warrant_private_9_3_changed.connect(self.on_input_gcws_warrant_private_9_3_changed)
        self._model.input_gcws_warrant_private_9_3_1_changed.connect(self.on_input_gcws_warrant_private_9_3_1_changed)
        self._model.input_gcws_warrant_private_9_3_2_a_changed.connect(self.on_input_gcws_warrant_private_9_3_2_a_changed)
        self._model.input_gcws_warrant_private_9_3_2_b_changed.connect(self.on_input_gcws_warrant_private_9_3_2_b_changed)
        self._model.input_gcws_warrant_private_9_3_2_c_changed.connect(self.on_input_gcws_warrant_private_9_3_2_c_changed)
        self._model.input_gcws_warrant_public_9_1_changed.connect(self.on_input_gcws_warrant_public_9_1_changed)
        self._model.input_gcws_warrant_public_9_1_a_changed.connect(self.on_input_gcws_warrant_public_9_1_a_changed)
        self._model.input_gcws_warrant_public_9_1_b_changed.connect(self.on_input_gcws_warrant_public_9_1_b_changed)
        self._model.input_gcws_warrant_public_9_1_c_changed.connect(self.on_input_gcws_warrant_public_9_1_c_changed)
        self._model.input_gcws_warrant_public_9_1_d_i_changed.connect(self.on_input_gcws_warrant_public_9_1_d_i_changed)
        self._model.input_gcws_warrant_public_9_1_d_ii_changed.connect(self.on_input_gcws_warrant_public_9_1_d_ii_changed)
        self._model.input_gcws_warrant_public_9_1_d_iii_changed.connect(self.on_input_gcws_warrant_public_9_1_d_iii_changed)
        self._model.input_gcws_warrant_sidewalk_9_5_changed.connect(self.on_input_gcws_warrant_sidewalk_9_5_changed)
        self._model.input_gates_gcws_warrant_private_9_4_1_a_changed.connect(self.on_input_gates_gcws_warrant_private_9_4_1_a_changed)
        self._model.input_gates_gcws_warrant_private_9_4_1_b_changed.connect(self.on_input_gates_gcws_warrant_private_9_4_1_b_changed)
        self._model.input_gates_gcws_warrant_private_9_4_1_c_changed.connect(self.on_input_gates_gcws_warrant_private_9_4_1_c_changed)
        self._model.input_gates_gcws_warrant_public_9_2_1_a_changed.connect(self.on_input_gates_gcws_warrant_public_9_2_1_a_changed)
        self._model.input_gates_gcws_warrant_public_9_2_1_b_changed.connect(self.on_input_gates_gcws_warrant_public_9_2_1_b_changed)
        self._model.input_gates_gcws_warrant_public_9_2_1_c_changed.connect(self.on_input_gates_gcws_warrant_public_9_2_1_c_changed)
        self._model.input_gates_gcws_warrant_public_9_2_1_d_changed.connect(self.on_input_gates_gcws_warrant_public_9_2_1_d_changed)
        self._model.input_gates_gcws_warrant_public_9_2_1_e_changed.connect(self.on_input_gates_gcws_warrant_public_9_2_1_e_changed)
        self._model.input_gates_gcws_warrant_sidewalk_9_6_changed.connect(self.on_input_gates_gcws_warrant_sidewalk_9_6_changed)
        #input_gcws_warrants_comments_changed = None

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        #input_gcws_comments_changed = None
            
        #Group LineEdits
        #input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail_changed = None 
        #input_gcws_measure_warning_device_n_or_e_approach_distance_from_road_changed = None 
        #input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation_changed = None 
        #input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation_changed = None 
        #input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail_changed = None 
        #input_gcws_measure_warning_device_s_or_w_approach_distance_from_road_changed = None 
        #input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation_changed = None 
        #input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation_changed = None 
        #input_gcws_rail_crossing_warning_time_actual_changed = None 

        #Group ComboBox
        #input_gcws_observe_bell_if_sidewalk_changed = None
        #input_gcws_observe_bells_condition_changed = None
        #input_gcws_observe_bells_n_or_e_approach_changed = None
        #input_gcws_observe_bells_s_or_w_approach_changed = None
        #input_gcws_observe_cantilever_lights_condition_changed = None
        #input_gcws_observe_cantilever_lights_n_or_e_approach_changed = None
        #input_gcws_observe_cantilever_lights_s_or_w_approach_changed = None
        #input_gcws_observe_gates_condition_changed = None
        #input_gcws_observe_gates_n_or_e_approach_changed = None
        #input_gcws_observe_gates_s_or_w_approach_changed = None
        #input_gcws_observe_gcws_limited_use_with_walk_light_assembly_changed = None
        #input_gcws_observe_gcws_limited_use_without_walk_light_assembly_changed = None
        #input_gcws_observe_light_units_condition_changed = None
        #input_gcws_observe_light_units_n_or_e_approach_changed = None
        #input_gcws_observe_light_units_s_or_w_approach_changed = None
        #input_gcws_observe_warning_time_consistency_changed = None   
        #input_gcws_observe_warning_time_consistency_reduced_speed_changed = None
        #input_gcws_rail_cut_out_circuit_requirements_changed = None
        #input_gcws_rail_directional_stick_circuit_requirements_changed = None
        #input_gcws_rail_self_diagnostic_changed = None

        #Group Labels
        self._model.input_gcws_rail_design_approach_warning_time_changed.connect(self.on_input_gcws_rail_design_approach_warning_time_changed)
        self._model.input_gcws_rail_design_warning_time_adjacent_crossing_changed.connect(self.on_input_gcws_rail_design_warning_time_adjacent_crossing_changed)
        self._model.input_gcws_rail_design_warning_time_clearance_distance_changed.connect(self.on_input_gcws_rail_design_warning_time_clearance_distance_changed)
        self._model.input_gcws_rail_design_warning_time_departure_time_pedestrian_changed.connect(self.on_input_gcws_rail_design_warning_time_departure_time_pedestrian_changed)
        self._model.input_gcws_rail_design_warning_time_departure_time_vehicle_changed.connect(self.on_input_gcws_rail_design_warning_time_departure_time_vehicle_changed)
        self._model.input_gcws_rail_design_warning_time_gate_arm_clearance_changed.connect(self.on_input_gcws_rail_design_warning_time_gate_arm_clearance_changed)
        self._model.input_gcws_rail_design_warning_time_preemption_changed.connect(self.on_input_gcws_rail_design_warning_time_preemption_changed)
        self._model.input_gcws_rail_design_warning_time_ssd_changed.connect(self.on_input_gcws_rail_design_warning_time_ssd_changed)

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        #input_light_units_comments_changed = None

        #Group LineEdits
        #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail_changed = None 
        #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road_changed = None 
        #input_light_units_measure_cantilevers_n_or_e_approach_dl_changed = None 
        #input_light_units_measure_cantilevers_n_or_e_approach_dr_changed = None 
        #input_light_units_measure_cantilevers_n_or_e_approach_height_changed = None 
        #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail_changed = None 
        #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road_changed = None 
        #input_light_units_measure_cantilevers_s_or_w_approach_dl_changed = None 
        #input_light_units_measure_cantilevers_s_or_w_approach_dr_changed = None 
        #input_light_units_measure_cantilevers_s_or_w_approach_height_changed = None 
        #input_light_units_measure_n_or_e_approach_height_changed = None 
        #input_light_units_measure_s_or_w_approach_height_changed = None 

        #Group ComboBoxes
        #input_light_units_observe_cantilevers_per_fig_12_3_changed = None
        #input_light_units_observe_per_fig_12_1_changed = None
        #input_light_units_observe_sidewalks_n_or_e_approach_changed = None
        #input_light_units_observe_sidewalks_s_or_w_approach_changed = None
        #input_light_units_observe_supplemental_lights_n_or_e_approach_changed = None
        #input_light_units_observe_supplemental_lights_s_or_w_approach_changed = None
        #input_light_units_observe_visibility_back_lights_n_or_e_approach_changed = None
        #input_light_units_observe_visibility_back_lights_s_or_w_approach_changed = None
        #input_light_units_observe_visibility_front_lights_n_or_e_approach_changed = None
        #input_light_units_observe_visibility_front_lights_s_or_w_approach_changed = None

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        #input_gates_gcws_comments_changed = None

        #Group LineEdits
        #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach_changed = None 
        #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach_changed = None 
        #input_gates_gcws_measure_gate_ascent_time_changed = None 
        #input_gates_gcws_measure_gate_descent_time_changed = None 
        #input_gates_gcws_rail_gate_arm_delay_time_design_changed = None 
        self._model.input_gates_gcws_rail_gate_arm_descent_time_design_changed.connect(self.on_input_gates_gcws_rail_gate_arm_descent_time_design_changed) 
        #input_gates_gcws_rail_inner_gate_arm_delay_time_design_changed = None 

        #Group Labels
        self._model.input_gates_gcws_calculate_gate_arm_clearance_time_recommended_changed.connect(self.on_input_gates_gcws_calculate_gate_arm_clearance_time_recommended_changed)
        self._model.input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended_changed.connect(self.on_input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended_changed)

        #Group ComboBoxes
        #input_gates_gcws_observe_gate_arm_rest_changed = None
        #input_gates_gcws_observe_gate_ascent_time_changed = None
        #input_gates_gcws_observe_gate_descent_time_changed = None
        #input_gates_gcws_observe_gate_strips_n_or_e_approach_changed = None
        #input_gates_gcws_observe_gate_strips_s_or_w_approach_changed = None
        #input_gates_gcws_observe_per_fig_12_2_changed = None

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        #input_aawd_comments_changed = None

        #Group LineEdits
        #input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual_changed = None 
        #input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual_changed = None 

        #Group ComboBoxes
        #input_aawd_observe_present_n_or_e_approach_changed = None
        #input_aawd_observe_present_s_or_w_approach_changed = None
        #input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach_changed = None
        #input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach_changed = None

        #Group Labels
        self._model.input_aawd_calculate_advance_activation_time_design_n_or_e_approach_changed.connect(self.on_input_aawd_calculate_advance_activation_time_design_n_or_e_approach_changed)
        self._model.input_aawd_calculate_advance_activation_time_design_s_or_w_approach_changed.connect(self.on_input_aawd_calculate_advance_activation_time_design_s_or_w_approach_changed)
        self._model.input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended_changed.connect(self.on_input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended_changed)
        self._model.input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended_changed.connect(self.on_input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended_changed)
        self._model. input_aawd_warrant_gcr_lookup_road_classification_changed.connect(self.on_input_aawd_warrant_gcr_lookup_road_classification_changed)
        self._model.input_aawd_warrant_gcr_observe_environmental_condition_changed.connect(self.on_input_aawd_warrant_gcr_observe_environmental_condition_changed)
        self._model.input_aawd_warrant_gcr_observe_sightline_obstruction_changed.connect(self.on_input_aawd_warrant_gcr_observe_sightline_obstruction_changed)
        self._model.input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr_changed.connect(self.on_input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr_changed)
        self._model.input_aawd_warrant_mutcd_lookup_significant_road_downgrade_changed.connect(self.on_input_aawd_warrant_mutcd_lookup_significant_road_downgrade_changed)

        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        #input_preemption_of_traffic_signals_comments_changed = None

        #Group LineEdits
        #input_preemption_of_traffic_signals_road_preemption_warning_time_actual_changed = None 
        #input_preemption_of_traffic_signals_road_preemption_warning_time_design_changed = None 

        #Group CombBoxes
        #input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles_changed = None
        #input_preemption_of_traffic_signals_observe_known_queuing_issues_changed = None
        #input_preemption_of_traffic_signals_observe_pedestrian_accommodation_changed = None
        #input_preemption_of_traffic_signals_observe_queuing_condition_changed = None
        #input_preemption_of_traffic_signals_observe_supplemental_signage_changed = None
        #input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate_changed = None
        #input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals_changed = None
        #input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type_changed = None

        #Group DatePicker
        #input_preemption_of_traffic_signals_road_date_Last_preemption_check_changed = None

        #Group Labels
        self._model.input_preemption_of_traffic_signals_lookup_proximity_condition_changed.connect(self.on_input_preemption_of_traffic_signals_lookup_proximity_condition_changed)
        self._model.input_preemption_of_traffic_signals_lookup_required_changed.connect(self.on_input_preemption_of_traffic_signals_lookup_required_changed)

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        #input_areas_without_train_whistling_comments_changed = None

        #Group ComboBoxes
        #input_areas_without_train_whistling_observe_for_stop_and_proceed_changed = None
        #input_areas_without_train_whistling_observe_tresNoneing_area_changed = None
        #input_areas_without_train_whistling_rail_anti_whistling_zone_changed = None
        #input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs_changed = None

        #Group Labels
        self._model.input_areas_without_train_whistling_lookup_gcs_12_to_16_changed.connect(self.on_input_areas_without_train_whistling_lookup_gcs_12_to_16_changed)
        self._model.input_areas_without_train_whistling_lookup_gcs_9_2_changed.connect(self.on_input_areas_without_train_whistling_lookup_gcs_9_2_changed)
        self._model.input_areas_without_train_whistling_requirements_observe_table_D1_changed.connect(self.on_input_areas_without_train_whistling_requirements_observe_table_D1_changed)

    #######################
    # SET UI-WIDGET SLOTS #
    #######################
    
    # INSPECTION DETAILS
    #Group TextBoxes
    #input_inspection_details_assessment_team_changed = None
    
    #Group DatePicker
    #input_inspection_details_date_assessment_changed = None
    
    #Group LineEdits
    #input_inspection_details_crossing_location_changed = None 
    #input_inspection_details_location_number_changed = None 
    #input_inspection_details_municipality_changed = None 
    #input_inspection_details_road_name_changed = None 
    #input_inspection_details_road_number_changed = None 
    #input_inspection_details_spur_name_changed = None  

    #Group DoubleSpinBox
    #input_inspection_details_latitude_changed = None
    #input_inspection_details_longitude_changed = None 
    #input_inspection_details_spur_mile_changed = None  
    #input_inspection_details_subdivision_mile_changed = None

    #Group ComboBoxes
    @qtc.pyqtSlot(list)
    def on_input_inspection_details_gcws_type_changed(self, value):
        self.comboBox_inspection_details_gcws_type.setValue(value)
    
    @qtc.pyqtSlot(list)
    def on_input_inspection_details_grade_crossing_type_changed(self, value):
        self.comboBox_inspection_details_grade_crossing_type.setValue(value)

    #input_inspection_details_province_changed = None
    #input_inspection_details_railway_authority_changed = None
    #input_inspection_details_reason_for_assessment_changed = None
    #input_inspection_details_road_authority_changed = None
    #input_inspection_details_subdivision_name_changed = None
    #input_inspection_details_track_type_changed = None

    # COLLISION HISTORY (5 YEAR PERIOD)
    #Group TextEdits
    #input_collision_history_comments_changed = None

    #Group SpinBox
    @qtc.pyqtSlot(int)
    def on_input_collision_history_fatal_injury_changed(self, value):
        self.spinBox_collision_history_fatal_injury.setValue(value)

    #input_collision_history_fatalities_changed = None 
    #input_collision_history_personal_injuries_changed = None 

    @qtc.pyqtSlot(int)
    def on_input_collision_history_personal_injury_changed(self, value):
        self.spinBox_collision_history_personal_injury.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_collision_history_property_damage_changed(self, value):
        self.spinBox_collision_history_property_damage.setValue(value)

    #Group Labels
    @qtc.pyqtSlot(int)
    def on_input_collision_history_total_5_year_period_changed(self, value):
        self.label_collision_history_total_5_year_period.setNum(value)

    # GENERAL INFORMATION
    #Group TextEdits
    #input_general_info_comments_changed = None

    #Group LineEdits
    #input_general_info_observe_special_buildings_changed = None
    #input_general_info_road_other_users_changed = None 

    #Group SpinBox
    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_max_railway_operating_speed_freight_changed(self, value):
        self.spinBox_general_info_rail_max_railway_operating_speed_freight.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_max_railway_operating_speed_passenger_changed(self, value):
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger.setValue(value)
    
    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_no_trains_per_day_freight_changed(self, value):
        self.spinBox_general_info_rail_no_trains_per_day_freight.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_no_trains_per_day_passengers_changed(self, value):
        self.spinBox_general_info_rail_no_trains_per_day_passengers.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_no_tracks_main_changed(self, value):
        self.spinBox_general_info_rail_no_tracks_main.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_no_tracks_other_changed(self, value):
        self.spinBox_general_info_rail_no_tracks_other.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_railway_design_speed_changed(self, value):
        self.spinBox_general_info_rail_railway_design_speed.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_road_aadt_current_changed(self, value):
        self.spinBox_general_info_road_aadt_current.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_road_aadt_forecast_changed(self, value):
        self.spinBox_general_info_road_aadt_forecast.setValue(value)

    #input_general_info_road_aadt_year_current_changed = None 
    #input_general_info_road_aadt_year_forecasted_changed = None 
    #input_general_info_road_cyclist_per_day_changed = None 
    
    @qtc.pyqtSlot(int)
    def on_input_general_info_road_no_traffic_lanes_bidirectional_changed(self, value):
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional.setValue(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_road_no_traffic_lanes_northbound_or_eastbound_changed(self, value):
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound.setValue(value)
        
    @qtc.pyqtSlot(int)
    def on_input_general_info_road_no_traffic_lanes_southbound_or_westbound_changed(self, value):
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound.setValue(value)
 
    #input_general_info_road_other_users_daily_users_changed = None 
    #input_general_info_road_pedestrians_per_day_changed = None 

    @qtc.pyqtSlot(int)
    def on_input_general_info_road_speed_design_changed(self, value):
        self.spinBox_general_info_road_speed_design.setValue(value)

    #input_general_info_road_speed_posted_changed = None 

    #Group ComboBoxes
    #input_general_info_observe_roadway_illumination_changed = None
    #input_general_info_observe_surrounding_land_use_changed = None
    #input_general_info_rail_train_switching_changed = None        
    #input_general_info_road_assistive_pedestrian_devices_changed = None
    
    @qtc.pyqtSlot(list)
    def on_input_general_info_road_classification_changed(self, value):
        self.comboBox_general_info_road_classification.clear()
        self.comboBox_general_info_road_classification.addItems(value)

    #input_general_info_road_dangerous_goods_route_changed = None
    #input_general_info_road_school_bus_route_changed = None
    #input_general_info_road_seasonal_volume_fluctuations_changed = None

    @qtc.pyqtSlot(list)
    def on_input_general_info_road_sidewalks_changed(self, value):
        self.comboBox_general_info_road_sidewalks.clear()
        self.comboBox_general_info_road_sidewalks.addItems(value)

    #Group Labels
    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_no_tracks_total_changed(self, value):
        self.label_general_info_rail_no_tracks_total.setText(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_rail_no_trains_per_day_total_changed(self, value):
        self.label_general_info_rail_no_trains_per_day_total.setText(value)

    @qtc.pyqtSlot(int)
    def on_input_general_info_road_no_traffic_lanes_total_changed(self, value):
        self.label_general_info_road_no_traffic_lanes_total.setText(value)

    # DESIGN CONSIDERATIONS (GCS SECTION 10)
    #Group TextEdits
    #input_design_comments_changed = None

    #Group DoubleSpinBox
    @qtc.pyqtSlot(float)
    def on_input_design_measure_adjacent_track_clearance_distance_changed(self, value):
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_design_measure_adjacent_track_separation_distance_changed(self, value):
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_design_measure_clearance_distance_pedestrian_changed(self, value):
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_design_measure_clearance_distance_vehicle_changed(self, value):
        self.doubleSpinBox_design_measure_clearance_distance_vehicle.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_design_road_max_approach_grade_within_s_changed(self, value):
        self.doubleSpinBox_design_road_max_approach_grade_within_s.setValue(value)

    #Group ComboBoxes
    #input_design_observe_field_acceleration_times_exceed_td = None

    @qtc.pyqtSlot(list)
    def on_input_design_road_design_vehicle_type_changed(self, value):
        self.comboBox_design_road_design_vehicle_type.clear()
        self.comboBox_design_road_design_vehicle_type.addItems(value)

    #Group Labels
    @qtc.pyqtSlot(float)
    def on_input_design_calculate_adjacent_track_clearance_time_changed(self, value):
        self.label_design_calculate_adjacent_track_clearance_time.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_calculate_clearance_time_crossing_pedestrian_design_check_changed(self, value):
        self.label_design_calculate_clearance_time_crossing_pedestrian_design_check.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_calculate_clearance_time_crossing_vehicle_design_check_changed(self, value):
        self.label_design_calculate_clearance_time_crossing_vehicle_design_check.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_calculate_clearance_time_gate_arm_ssd_changed(self, value):
        self.label_design_calculate_clearance_time_gate_arm_ssd.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_calculate_clearance_time_gate_arm_stop_changed(self, value):
        self.label_design_calculate_clearance_time_gate_arm_stop.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_calculate_vehicle_travel_distance_changed(self, value):
        self.label_design_calculate_vehicle_travel_distance.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_input_reaction_time_changed(self, value):
        self.label_design_input_reaction_time.setNum(value)

    @qtc.pyqtSlot(str)
    def on_input_design_lookup_design_vehicle_class_changed(self, value):
        self.label_design_lookup_design_vehicle_class.setText(value)

    @qtc.pyqtSlot(float)
    def on_input_design_lookup_design_vehicle_length_changed(self, value):
        self.label_design_lookup_design_vehicle_length.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_lookup_grade_adjustment_factor_changed(self, value):
        self.label_design_lookup_grade_adjustment_factor.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_lookup_vehicle_departure_time_crossing_changed(self, value):
        self.label_design_lookup_vehicle_departure_time_crossing.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_design_lookup_vehicle_departure_time_gate_arm_clearance_changed(self, value):
        self.label_design_lookup_vehicle_departure_time_gate_arm_clearance.setNum(value)
    
    # LOCATION OF GRADE CROSSING (GCS SECTION 11)
    #Group TextEdits
    #input_location_of_grade_crossing_comments_changed = None

    #Group DoubleSpinBox
    #input_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach_changed = None 
    #input_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach_changed = None 
    
    @qtc.pyqtSlot(float)
    def on_input_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach_changed(self, value):
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach.setValue(value)
    
    @qtc.pyqtSlot(float)
    def on_input_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach_changed(self, value):
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach.setValue(value)
        
    @qtc.pyqtSlot(float)
    def on_input_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach_changed(self, value):
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach_changed(self, value):
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach.setValue(value)

    #group ComboBoxes
    #input_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk_changed = None
    #input_location_of_grade_crossing_queue_condition_changed = None
    #input_location_of_grade_crossing_visibility_of_warning_lights_changed = None
    
    # GRADE CROSSING SURFACE (GCS SECTION 5)
    #Group TextEdits
    #input_grade_crossing_surface_comments_changed = None

    #Group DoubleSpinBox
    #input_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_crossing_surface_width_changed = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface_changed = None 
    #input_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface_changed = None 
    #input_grade_crossing_surface_measure_flangeway_depth_changed = None 
    #input_grade_crossing_surface_measure_flangeway_width_changed = None 
    #input_grade_crossing_surface_measure_road_surface_median_width_changed = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_side_grinding_depth_changed = None 
    #input_grade_crossing_surface_measure_side_grinding_width_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach_changed = None 
    #input_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach_changed = None 

    #Group ComboBoxes
    #input_grade_crossing_surface_observe_crossing_smoothness_changed = None
    #input_grade_crossing_surface_observe_crossing_surface_condition_changed = None
    #input_grade_crossing_surface_observe_material_changed = None
    #input_grade_crossing_surface_observe_road_approach_surface_condition_changed = None
    #input_grade_crossing_surface_observe_road_approach_surface_type_changed = None

    # ROAD GEOMETRY (GCS SECTION 6)
    #Group TextEdits 
    #input_road_geometry_comments_changed = None

    #Group DoubleSpinBox
    @qtc.pyqtSlot(float)
    def on_input_road_geometry_measure_railway_cross_slope_changed(self, value):
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope.setValue(value)

    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach_changed = None 
    #input_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach_changed = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach_changed = None 
    #input_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach_changed = None
    
    @qtc.pyqtSlot(float)
    def on_input_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach_changed(self, value):
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach.setValue(value) 
    
    @qtc.pyqtSlot(float)
    def on_input_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach_changed(self, value):
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_road_geometry_rail_superelevation_n_or_e_approach_changed(self, value):
        self.doubleSpinBox_road_geometry_rail_superelevation_n_or_e_approach.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_road_geometry_rail_superelevation_s_or_w_approach_changed(self, value):
        self.doubleSpinBox_road_geometry_rail_superelevation_s_or_w_approach.setValue(value)

    #input_road_geometry_road_crossing_angle_changed = None 

    @qtc.pyqtSlot(float)
    def on_input_road_geometry_road_general_approach_grade_n_or_e_approach_changed(self, value):
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach.setValue(value)

    @qtc.pyqtSlot(float)
    def on_input_road_geometry_road_general_approach_grade_s_or_w_approach_changed(self, value):
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach.setValue(value)

    #Group ComboBoxes
    #input_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach_changed = None
    #input_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach_changed = None
    #input_road_geometry_observe_low_bed_truck_condition_changed = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach_changed = None
    #input_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach_changed = None
    
    #Group Labels
    @qtc.pyqtSlot(float)
    def on_input_road_geometry_lookup_gradient_difference_changed(self, value):
        self.label_road_geometry_lookup_gradient_difference.setNum(value)
    
    # SIGHTLINES (GCS SECTION 7)
    #Group TextEdits
    #input_sightlines_comments_changed = None
    
    #Group LineEdits
    #input_sightlines_measure_dssd_actual_n_or_e_approach_left_changed = None 
    #input_sightlines_measure_dssd_actual_n_or_e_approach_right_changed = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_left_changed = None 
    #input_sightlines_measure_dssd_actual_s_or_w_approach_right_changed = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left_changed = None 
    #input_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right_changed = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left_changed = None 
    #input_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right_changed = None 
    #input_sightlines_measure_ssd_actual_n_or_e_approach_changed = None 
    #input_sightlines_measure_ssd_actual_s_or_w_approach_changed = None 

    #Group ComboBoxes
    #input_sightlines_observe_sightline_obstructions_changed = None

    #Group Labels
    @qtc.pyqtSlot(float)
    def on_input_sightlines_calculate_dssd_vehicle_min_ft_changed(self, value):
        self.label_sightlines_calculate_dssd_vehicle_min_ft.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_calculate_dssd_vehicle_min_m_changed(self, value):
        self.label_sightlines_calculate_dssd_vehicle_min_m.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_calculate_dstopped_pedestrian_min_ft_changed(self, value):
        self.label_sightlines_calculate_dstopped_pedestrian_min_ft.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_calculate_dstopped_pedestrian_min_m_changed(self, value):
        self.label_sightlines_calculate_dstopped_pedestrian_min_m.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_calculate_dstopped_vehicle_min_ft_changed(self, value):
        self.label_sightlines_calculate_dstopped_vehicle_min_ft.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_calculate_dstopped_vehicle_min_m_changed(self, value):
        self.label_sightlines_calculate_dstopped_vehicle_min_m.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_lookup_ssd_minimum_n_or_e_approach_changed(self, value):
        self.label_sightlines_lookup_ssd_minimum_n_or_e_approach.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_sightlines_lookup_ssd_minimum_s_or_w_approach_changed(self, value):
        self.label_sightlines_lookup_ssd_minimum_s_or_w_approach.setNum(value)

    # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
    #Group TextEdits
    #DELETE input_signs_and_markings_advisory_speed_comments_changed = None
    #DELETE input_signs_and_markings_comments_changed = None
    #DELETE input_signs_and_markings_emergency_notification_comments_changed = None
    #DELETE input_signs_and_markings_number_of_tracks_comments_changed = None
    #DELETE input_signs_and_markings_railway_crossing_ahead_comments_changed = None
    #DELETE input_signs_and_markings_railway_crossing_comments_changed = None
    #DELETE input_signs_and_markings_stop_comments_changed = None
    #DELETE input_signs_and_markings_stop_sign_ahead_comments_changed = None

    #Group DoubleSpinBox
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road_changed = None 
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height_changed = None 
    #input_signs_and_markings_stop_n_or_e_approach_height_changed = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_n_or_e_approach_location_from_road_changed = None 
    #input_signs_and_markings_stop_s_or_w_approach_height_changed = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_s_or_w_approach_location_from_road_changed = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_height_changed = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road_changed = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_height_changed = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail_changed = None 
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road_changed = None 

    #Group ComboBoxes
    #input_signs_and_markings_advisory_speed_n_or_e_approach_present_changed = None
    #input_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20_changed = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_present_changed = None
    #input_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20_changed = None
    #input_signs_and_markings_dividing_lines_present_changed = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_condition_changed = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_legible_changed = None
    #input_signs_and_markings_emergency_Notification_n_or_e_approach_orientation_changed = None
    #input_signs_and_markings_emergency_notification_n_or_e_approach_present_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_condition_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_legible_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_orientation_changed = None
    #input_signs_and_markings_emergency_notification_s_or_w_approach_present_changed = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b_changed = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c_changed = None
    #input_signs_and_markings_number_of_tracks_n_or_e_approach_present_changed = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b_changed = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c_changed = None
    #input_signs_and_markings_number_of_tracks_s_or_w_approach_present_changed = None
    #input_signs_and_markings_per_mutcd_changed = None
    #input_signs_and_markings_posted_speed_n_or_e_approach_present_changed = None
    #input_signs_and_markings_posted_speed_s_or_w_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation_changed = None
    #input_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation_changed = None
    #input_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a_changed = None
    #input_signs_and_markings_railway_crossing_n_or_e_approach_present_changed = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a_changed = None
    #input_signs_and_markings_railway_crossing_s_or_w_approach_present_changed = None
    #input_signs_and_markings_sidewalks_present_changed = None
    #input_signs_and_markings_stop_n_or_e_approach_per_fig_8_4_changed = None
    #input_signs_and_markings_stop_n_or_e_approach_present_changed = None
    #input_signs_and_markings_stop_n_or_e_approach_same_post_changed = None
    #input_signs_and_markings_stop_s_or_w_approach_per_fig_8_4_changed = None
    #input_signs_and_markings_stop_s_or_w_approach_present_changed = None
    #input_signs_and_markings_stop_s_or_w_approach_same_post_changed = None
    #input_signs_and_markings_stop_sign_ahead_n_or_e_approach_present_changed = None
    #input_signs_and_markings_stop_sign_ahead_s_or_w_approach_present_changed = None

    # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
    # Group Labels
    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_private_9_3_changed(self, value):
        self.label_gcws_warrant_private_9_3.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_private_9_3_1_changed(self, value):
        self.label_gcws_warrant_private_9_3_1.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_private_9_3_2_a_changed(self, value):
        self.label_gcws_warrant_private_9_3_2_a.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_private_9_3_2_b_changed(self, value):
        self.label_gcws_warrant_private_9_3_2_b.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_private_9_3_2_c_changed(self, value):
        self.label_gcws_warrant_private_9_3_2_c.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_changed(self, value):
        self.label_gcws_warrant_public_9_1.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_a_changed(self, value):
        self.label_gcws_warrant_public_9_1_a.setText(value)
        
    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_b_changed(self, value):
        self.label_gcws_warrant_public_9_1_b.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_c_changed(self, value):
        self.label_gcws_warrant_public_9_1_c.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_d_i_changed(self, value):
        self.label_gcws_warrant_public_9_1_d_i.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_d_ii_changed(self, value):
        self.label_gcws_warrant_public_9_1_d_ii.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_public_9_1_d_iii_changed(self, value):
        self.label_gcws_warrant_public_9_1_d_iii.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gcws_warrant_sidewalk_9_5_changed(self, value):
        self.label_gcws_warrant_sidewalk_9_5.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_private_9_4_1_a_changed(self, value):
        self.label_gates_gcws_warrant_private_9_4_1_a.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_private_9_4_1_b_changed(self, value):
        self.label_gates_gcws_warrant_private_9_4_1_b.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_private_9_4_1_c_changed(self, value):
        self.label_gates_gcws_warrant_private_9_4_1_c.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_public_9_2_1_a_changed(self, value):
        self.label_gates_gcws_warrant_public_9_2_1_a.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_public_9_2_1_b_changed(self, value):
        self.label_gates_gcws_warrant_public_9_2_1_b.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_public_9_2_1_c_changed(self, value):
        self.label_gates_gcws_warrant_public_9_2_1_c.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_public_9_2_1_d_changed(self, value):
        self.label_gates_gcws_warrant_public_9_2_1_d.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_public_9_2_1_e_changed(self, value):
        self.label_gates_gcws_warrant_public_9_2_1_e.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_gates_gcws_warrant_sidewalk_9_6_changed(self, value):
        self.label_gates_gcws_warrant_sidewalk_9_6.setText(value)

    #input_gcws_warrants_comments_changed = None

    # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
    #Group TextEdits
    #input_gcws_comments_changed = None
        
    #Group DoubleSpinBox
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_rail_changed = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_from_road_changed = None 
    #input_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation_changed = None 
    #input_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_rail_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_from_road_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation_changed = None 
    #input_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation_changed = None 
    #input_gcws_rail_crossing_warning_time_actual_changed = None 

    #Group ComboBox
    #input_gcws_observe_bell_if_sidewalk_changed = None
    #input_gcws_observe_bells_condition_changed = None
    #input_gcws_observe_bells_n_or_e_approach_changed = None
    #input_gcws_observe_bells_s_or_w_approach_changed = None
    #input_gcws_observe_cantilever_lights_condition_changed = None
    #input_gcws_observe_cantilever_lights_n_or_e_approach_changed = None
    #input_gcws_observe_cantilever_lights_s_or_w_approach_changed = None
    #input_gcws_observe_gates_condition_changed = None
    #input_gcws_observe_gates_n_or_e_approach_changed = None
    #input_gcws_observe_gates_s_or_w_approach_changed = None
    #input_gcws_observe_gcws_limited_use_with_walk_light_assembly_changed = None
    #input_gcws_observe_gcws_limited_use_without_walk_light_assembly_changed = None
    #input_gcws_observe_light_units_condition_changed = None
    #input_gcws_observe_light_units_n_or_e_approach_changed = None
    #input_gcws_observe_light_units_s_or_w_approach_changed = None
    #input_gcws_observe_warning_time_consistency_changed = None   
    #input_gcws_observe_warning_time_consistency_reduced_speed_changed = None
    #input_gcws_rail_cut_out_circuit_requirements_changed = None
    #input_gcws_rail_directional_stick_circuit_requirements_changed = None
    #input_gcws_rail_self_diagnostic_changed = None

    #Group Labels
    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_approach_warning_time_changed(self, value):
        self.label_gcws_rail_design_approach_warning_time.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_adjacent_crossing_changed(self, value):
        self.label_gcws_rail_design_warning_time_adjacent_crossing.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_clearance_distance_changed(self, value):
        self.label_gcws_rail_design_warning_time_clearance_distance.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_departure_time_pedestrian_changed(self, value):
        self.label_gcws_rail_design_warning_time_departure_time_pedestrian.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_departure_time_vehicle_changed(self, value):
        self.label_gcws_rail_design_warning_time_departure_time_vehicle.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_gate_arm_clearance_changed(self, value):
        self.label_gcws_rail_design_warning_time_gate_arm_clearance.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_preemption_changed(self, value):
        self.label_gcws_rail_design_warning_time_preemption.setNum(value)
        
    @qtc.pyqtSlot(float)
    def on_input_gcws_rail_design_warning_time_ssd_changed(self, value):
        self.label_gcws_rail_design_warning_time_ssd.setNum(value)

    # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
    #Group TextEdits
    #input_light_units_comments_changed = None

    #Group LineEdits
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_distance_from_road_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dl_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_dr_changed = None 
    #input_light_units_measure_cantilevers_n_or_e_approach_height_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_distance_from_road_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dl_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_dr_changed = None 
    #input_light_units_measure_cantilevers_s_or_w_approach_height_changed = None 
    #input_light_units_measure_n_or_e_approach_height_changed = None 
    #input_light_units_measure_s_or_w_approach_height_changed = None 

    #Group ComboBoxes
    #input_light_units_observe_cantilevers_per_fig_12_3_changed = None
    #input_light_units_observe_per_fig_12_1_changed = None
    #input_light_units_observe_sidewalks_n_or_e_approach_changed = None
    #input_light_units_observe_sidewalks_s_or_w_approach_changed = None
    #input_light_units_observe_supplemental_lights_n_or_e_approach_changed = None
    #input_light_units_observe_supplemental_lights_s_or_w_approach_changed = None
    #input_light_units_observe_visibility_back_lights_n_or_e_approach_changed = None
    #input_light_units_observe_visibility_back_lights_s_or_w_approach_changed = None
    #input_light_units_observe_visibility_front_lights_n_or_e_approach_changed = None
    #input_light_units_observe_visibility_front_lights_s_or_w_approach_changed = None

    # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
    #Group TextEdits
    #input_gates_gcws_comments_changed = None

    #Group SpinBox
    #input_gates_gcws_measure_gate_ascent_time_changed = None 
    #input_gates_gcws_measure_gate_descent_time_changed = None 

    @qtc.pyqtSlot(float)
    def on_input_gates_gcws_rail_gate_arm_descent_time_design_changed(self, value):
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design.setValue(value)

    #input_gates_gcws_rail_gate_arm_delay_time_design_changed = None 
    #input_gates_gcws_rail_inner_gate_arm_delay_time_design_changed = None 

    #Group DoubleSpinBox
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach_changed = None 
    #input_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach_changed = None 
    
    #Group Labels
    @qtc.pyqtSlot(float)
    def on_input_gates_gcws_calculate_gate_arm_clearance_time_recommended_changed(self, value):
        self.label_gates_gcws_calculate_gate_arm_clearance_time_recommended.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_gates_gcws_calculate_inner_gate_arm_delay_time_recommended_changed(self, value):
        self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended.setNum(value)

    #Group ComboBoxes
    #input_gates_gcws_observe_gate_arm_rest_changed = None
    #input_gates_gcws_observe_gate_ascent_time_changed = None
    #input_gates_gcws_observe_gate_descent_time_changed = None
    #input_gates_gcws_observe_gate_strips_n_or_e_approach_changed = None
    #input_gates_gcws_observe_gate_strips_s_or_w_approach_changed = None
    #input_gates_gcws_observe_per_fig_12_2_changed = None

    # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
    #Group Text Edits
    #input_aawd_comments_changed = None

    #Group DoubleSpinBox
    #input_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual_changed = None 
    #input_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual_changed = None 

    #Group ComboBoxes
    #input_aawd_observe_present_n_or_e_approach_changed = None
    #input_aawd_observe_present_s_or_w_approach_changed = None
    #input_aawd_road_aawd_sufficient_activation_time_n_or_e_approach_changed = None
    #input_aawd_road_aawd_sufficient_activation_time_s_or_w_approach_changed = None

    #Group Labels
    @qtc.pyqtSlot(float)
    def on_input_aawd_calculate_advance_activation_time_design_n_or_e_approach_changed(self, value):
        self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_aawd_calculate_advance_activation_time_design_s_or_w_approach_changed(self, value):
        self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended_changed(self, value):
        self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended.setNum(value)

    @qtc.pyqtSlot(float)
    def on_input_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended_changed(self, value):
        self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended.setNum(value)

    @qtc.pyqtSlot(str)
    def on_input_aawd_warrant_gcr_lookup_road_classification_changed(self, value):
        self.label_aawd_warrant_gcr_lookup_road_classification.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_aawd_warrant_gcr_lookup_road_classification_changed(self, value):
        self.label_aawd_warrant_gcr_lookup_road_classification.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_aawd_warrant_gcr_observe_environmental_condition_changed(self, value):
        self.label_aawd_warrant_gcr_observe_environmental_condition.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_aawd_warrant_gcr_observe_sightline_obstruction_changed(self, value):
        self.label_aawd_warrant_gcr_observe_sightline_obstruction.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr_changed(self, value):
        self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_aawd_warrant_mutcd_lookup_significant_road_downgrade_changed(self, value):
        self.label_aawd_warrant_mutcd_lookup_significant_road_downgrade.setText(value)

    # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
    #Group TextEdits
    #input_preemption_of_traffic_signals_comments_changed = None

    #Group SpinBox
    #input_preemption_of_traffic_signals_road_preemption_warning_time_actual_changed = None 
    #input_preemption_of_traffic_signals_road_preemption_warning_time_design_changed = None 

    #Group CombBoxes
    #input_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles_changed = None
    #input_preemption_of_traffic_signals_observe_known_queuing_issues_changed = None
    #input_preemption_of_traffic_signals_observe_pedestrian_accommodation_changed = None
    #input_preemption_of_traffic_signals_observe_queuing_condition_changed = None
    #input_preemption_of_traffic_signals_observe_supplemental_signage_changed = None
    #input_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate_changed = None
    #input_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals_changed = None
    #input_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type_changed = None

    #Group DatePicker
    #input_preemption_of_traffic_signals_road_date_Last_preemption_check_changed = None

    #Group Labels
    @qtc.pyqtSlot(str)
    def on_input_preemption_of_traffic_signals_lookup_proximity_condition_changed(self, value):
        self.label_preemption_of_traffic_signals_lookup_proximity_condition.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_preemption_of_traffic_signals_lookup_required_changed(self, value):
        self.label_preemption_of_traffic_signals_lookup_required.setText(value)

    # WHISTLE CESSATION (GCS SECTION Appendix D)
    #Group TextEdits
    #input_areas_without_train_whistling_comments_changed = None

    #Group ComboBoxes
    #input_areas_without_train_whistling_observe_for_stop_and_proceed_changed = None
    #input_areas_without_train_whistling_observe_tresNoneing_area_changed = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone_changed = None
    #input_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs_changed = None

    #Group Labels
    @qtc.pyqtSlot(str)
    def on_input_areas_without_train_whistling_lookup_gcs_12_to_16_changed(self, value):
        self.label_areas_without_train_whistling_lookup_gcs_12_to_16.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_areas_without_train_whistling_lookup_gcs_9_2_changed(self, value):
        self.label_areas_without_train_whistling_lookup_gcs_9_2.setText(value)

    @qtc.pyqtSlot(str)
    def on_input_areas_without_train_whistling_requirements_observe_table_D1_changed(self, value):
        self.label_areas_without_train_whistling_requirements_observe_table_D1.setText(value)

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
        Create widgets that will be used in the application form. 
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
        self.textEdit_inspection_details_assessment_team = qtw.QTextEdit()
        
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
        self.lineEdit_inspection_details_crossing_location = qtw.QLineEdit()  
        self.lineEdit_inspection_details_location_number = qtw.QLineEdit() 
        self.lineEdit_inspection_details_municipality = qtw.QLineEdit() 
        self.lineEdit_inspection_details_road_name = qtw.QLineEdit() 
        self.lineEdit_inspection_details_road_number = qtw.QLineEdit() 
        self.lineEdit_inspection_details_spur_name = qtw.QLineEdit() 

        #Group DoubleSpinBox
        self.doubleSpinBox_inspection_details_latitude = qtw.QDoubleSpinBox ()
        self.doubleSpinBox_inspection_details_longitude = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_inspection_details_spur_mile = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_inspection_details_subdivision_mile = qtw.QDoubleSpinBox() 

        #Group ComboBoxes
        self.comboBox_inspection_details_gcws_type = qtw.QComboBox()
        self.comboBox_inspection_details_gcws_type.addItems(list_inspection_details_gcws_type)

        self.comboBox_inspection_details_grade_crossing_type = qtw.QComboBox()
        self.comboBox_inspection_details_grade_crossing_type.addItems(list_inspection_details_grade_crossing_type)

        self.comboBox_inspection_details_province = qtw.QComboBox()
        self.comboBox_inspection_details_province.addItems(list_inspection_details_province)

        self.comboBox_inspection_details_railway_authority = qtw.QComboBox()
        #TODO create and add railway authority list 

        self.comboBox_inspection_details_reason_for_assessment = qtw.QComboBox()
        self.comboBox_inspection_details_reason_for_assessment.addItems(list_inspection_details_reason_for_assessment)
        
        self.comboBox_inspection_details_road_authority = qtw.QComboBox()
        #TODO create and add road authority list 

        self.comboBox_inspection_details_subdivision_name = qtw.QComboBox()
        #TODO create and add subdivision list 

        self.comboBox_inspection_details_track_type = qtw.QComboBox()
        self.comboBox_inspection_details_track_type.addItems(list_inspection_details_track_type)

        # COLLISION HISTORY (5 YEAR PERIOD)
        #Group TextEdits
        self.textEdit_collision_history_comments = qtw.QTextEdit()

        #Group SpinBox
        self.spinBox_collision_history_fatal_injury = qtw.QSpinBox () 
        self.spinBox_collision_history_fatalities = qtw.QSpinBox () 
        self.spinBox_collision_history_personal_injuries = qtw.QSpinBox () 
        self.spinBox_collision_history_personal_injury = qtw.QSpinBox () 
        self.spinBox_collision_history_property_damage = qtw.QSpinBox ()

        #Group Labels 
        self.label_collision_history_total_5_year_period = qtw.QLabel()

        # GENERAL INFORMATION
        #Group TextEdits
        self.textEdit_general_info_comments = qtw.QTextEdit()

        #Group LineEdits
        self.lineEdit_general_info_observe_special_buildings = qtw.QLineEdit() 
        self.lineEdit_general_info_road_other_users = qtw.QLineEdit() 

        #Group SpinBox
        self.spinBox_general_info_rail_max_railway_operating_speed_freight = qtw.QSpinBox () 
        self.spinBox_general_info_rail_max_railway_operating_speed_passenger = qtw.QSpinBox () 
        self.spinBox_general_info_rail_no_tracks_main = qtw.QSpinBox () 
        self.spinBox_general_info_rail_no_tracks_other = qtw.QSpinBox ()
        self.spinBox_general_info_rail_no_trains_per_day_freight = qtw.QSpinBox () 
        self.spinBox_general_info_rail_no_trains_per_day_passengers = qtw.QSpinBox () 
        self.spinBox_general_info_rail_railway_design_speed = qtw.QSpinBox () 
        self.spinBox_general_info_road_aadt_current = qtw.QSpinBox () 
        self.spinBox_general_info_road_aadt_forecast = qtw.QSpinBox () 
        self.spinBox_general_info_road_aadt_year_current = qtw.QSpinBox () 
        self.spinBox_general_info_road_aadt_year_forecasted = qtw.QSpinBox () 
        self.spinBox_general_info_road_cyclist_per_day = qtw.QSpinBox () 
        self.spinBox_general_info_road_no_traffic_lanes_bidirectional = qtw.QSpinBox () 
        self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound = qtw.QSpinBox () 
        self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound = qtw.QSpinBox () 
        self.spinBox_general_info_road_other_users_daily_users = qtw.QSpinBox () 
        self.spinBox_general_info_road_pedestrians_per_day = qtw.QSpinBox () 
        self.spinBox_general_info_road_speed_design = qtw.QSpinBox () 
        self.spinBox_general_info_road_speed_posted = qtw.QSpinBox () 

        #Group ComboBoxes
        self.comboBox_general_info_observe_roadway_illumination = qtw.QComboBox()
        self.comboBox_general_info_observe_roadway_illumination.addItems(list_yes_no)

        self.comboBox_general_info_observe_surrounding_land_use = qtw.QComboBox()
        self.comboBox_general_info_observe_surrounding_land_use.addItems(list_general_info_observe_surrounding_land_use)

        self.comboBox_general_info_rail_train_switching = qtw.QComboBox()
        self.comboBox_general_info_rail_train_switching.addItems(list_yes_no)
        
        self.comboBox_general_info_road_assistive_pedestrian_devices = qtw.QComboBox()
        self.comboBox_general_info_road_assistive_pedestrian_devices.addItems(list_yes_no)

        self.comboBox_general_info_road_classification = qtw.QComboBox()
        self.comboBox_general_info_road_classification.addItems(list_general_info_road_classification)
        
        self.comboBox_general_info_road_dangerous_goods_route = qtw.QComboBox()
        self.comboBox_general_info_road_dangerous_goods_route.addItems(list_yes_no)

        self.comboBox_general_info_road_school_bus_route = qtw.QComboBox()
        self.comboBox_general_info_road_school_bus_route.addItems(list_yes_no)

        self.comboBox_general_info_road_seasonal_volume_fluctuations = qtw.QComboBox()
        self.comboBox_general_info_road_seasonal_volume_fluctuations.addItems(list_yes_no)

        self.comboBox_general_info_road_sidewalks = qtw.QComboBox()
        self.comboBox_general_info_road_sidewalks.addItems(list_yes_no)

        #Group Labels
        self.label_general_info_rail_no_tracks_total = qtw.QLabel()
        self.label_general_info_rail_no_trains_per_day_total = qtw.QLabel()
        self.label_general_info_road_no_traffic_lanes_total = qtw.QLabel()

        # DESIGN CONSIDERATIONS (GCS SECTION 10)
        #Group TextEdits
        self.textEdit_design_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_design_measure_adjacent_track_clearance_distance = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_design_measure_adjacent_track_separation_distance = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_design_measure_clearance_distance_pedestrian = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_design_measure_clearance_distance_vehicle = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_design_road_max_approach_grade_within_s = qtw.QDoubleSpinBox () 

        #Group ComboBoxes
        self.comboBox_design_observe_field_acceleration_times_exceed_td = qtw.QComboBox()
        self.comboBox_design_observe_field_acceleration_times_exceed_td.addItems(list_yes_no)

        self.comboBox_design_road_design_vehicle_type = qtw.QComboBox()
        self.comboBox_design_road_design_vehicle_type.addItems(list_design_road_design_vehicle_type)

        #Group Labels
        self.label_design_calculate_adjacent_track_clearance_time = qtw.QLabel()
        self.label_design_calculate_clearance_time_crossing_pedestrian_design_check = qtw.QLabel()
        self.label_design_calculate_clearance_time_crossing_vehicle_design_check = qtw.QLabel()
        self.label_design_calculate_clearance_time_gate_arm_ssd = qtw.QLabel()
        self.label_design_calculate_clearance_time_gate_arm_stop = qtw.QLabel()
        self.label_design_calculate_vehicle_travel_distance = qtw.QLabel()
        self.label_design_input_reaction_time = qtw.QLabel()
        self.label_design_lookup_design_vehicle_class = qtw.QLabel()
        self.label_design_lookup_design_vehicle_length = qtw.QLabel()
        self.label_design_lookup_grade_adjustment_factor = qtw.QLabel()
        self.label_design_lookup_vehicle_departure_time_crossing = qtw.QLabel()
        self.label_design_lookup_vehicle_departure_time_gate_arm_clearance = qtw.QLabel()
        
        # LOCATION OF GRADE CROSSING (GCS SECTION 11)
        #Group TextEdits
        self.textEdit_location_of_grade_crossing_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach = qtw.QDoubleSpinBox () 

        #group ComboBoxes
        self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk.addItems(list_yes_no)

        self.comboBox_location_of_grade_crossing_queue_condition = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_queue_condition.addItems(list_yes_no)

        self.comboBox_location_of_grade_crossing_visibility_of_warning_lights = qtw.QComboBox()
        self.comboBox_location_of_grade_crossing_visibility_of_warning_lights.addItems(list_yes_no)
        
        # GRADE CROSSING SURFACE (GCS SECTION 5)
        #Group TextEdits
        self.textEdit_grade_crossing_surface_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach = qtw.QDoubleSpinBox () 

        #Group ComboBoxes
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness.addItems(list_yes_no)

        self.comboBox_grade_crossing_surface_observe_crossing_surface_condition = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_crossing_smoothness.addItems(list_condition)

        self.comboBox_grade_crossing_surface_observe_material = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_material.addItems(list_grade_crossing_surface_observe_material)

        self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition.addItems(list_condition)

        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type = qtw.QComboBox()
        self.comboBox_grade_crossing_surface_observe_road_approach_surface_type.addItems(list_grade_crossing_surface_observe_road_approach_surface_type)

        # ROAD GEOMETRY (GCS SECTION 6)
        #Group TextEdits 
        self.textEdit_road_geometry_comments = qtw.QTextEdit()

        #Group SpinBox
        self.spinBox_road_geometry_road_crossing_angle = qtw.QSpinBox () 

        #Group DoubleSpinBox
        self.doubleSpinBox_road_geometry_measure_railway_cross_slope = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_rail_superelevation_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_rail_superelevation_s_or_w_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach = qtw.QDoubleSpinBox () 

        #Group ComboBoxes
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_low_bed_truck_condition = qtw.QComboBox()
        self.comboBox_road_geometry_observe_low_bed_truck_condition.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach = qtw.QComboBox()
        self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach.addItems(list_yes_no)
       
        #Group Labels
        self.label_road_geometry_lookup_gradient_difference = qtw.QLabel()
        
        # SIGHTLINES (GCS SECTION 7)
        #Group TextEdits
        self.textEdit_sightlines_comments = qtw.QTextEdit()
        
        #Group DoubleSpinBox
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach = qtw.QDoubleSpinBox() 

        #Group ComboBoxes
        self.comboBox_sightlines_observe_sightline_obstructions = qtw.QComboBox()
        self.comboBox_sightlines_observe_sightline_obstructions.addItems(list_yes_no)

        #Group Labels
        self.label_sightlines_calculate_dssd_vehicle_min_ft = qtw.QLabel()
        self.label_sightlines_calculate_dssd_vehicle_min_m = qtw.QLabel()
        self.label_sightlines_calculate_dstopped_pedestrian_min_ft = qtw.QLabel()
        self.label_sightlines_calculate_dstopped_pedestrian_min_m = qtw.QLabel()
        self.label_sightlines_calculate_dstopped_vehicle_min_ft = qtw.QLabel()
        self.label_sightlines_calculate_dstopped_vehicle_min_m = qtw.QLabel()
        self.label_sightlines_lookup_ssd_minimum_n_or_e_approach = qtw.QLabel()
        self.label_sightlines_lookup_ssd_minimum_s_or_w_approach = qtw.QLabel()

        # SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #Group TextEdits
        #DELETE self.textEdit_signs_and_markings_advisory_speed_comments = pass
        #DELETE self.textEdit_signs_and_markings_comments = pass
        #DELETE self.textEdit_signs_and_markings_emergency_notification_comments = pass
        #DELETE self.textEdit_signs_and_markings_number_of_tracks_comments = pass
        #DELETE self.textEdit_signs_and_markings_railway_crossing_ahead_comments = pass
        #DELETE self.textEdit_signs_and_markings_railway_crossing_comments = pass
        #DELETE self.textEdit_signs_and_markings_stop_comments = pass
        #DELETE self.textEdit_signs_and_markings_stop_sign_ahead_comments = pass

        #Group DoubleSpinBox
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail = qtw.QDoubleSpinBox() 
        self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road = qtw.QDoubleSpinBox() 

        #Group ComboBoxes
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20 = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20 = qtw.QComboBox()
        self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_dividing_lines_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_dividing_lines_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition.addItems(list_condition)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition.addItems(list_condition)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_per_mutcd = qtw.QComboBox()
        self.comboBox_signs_and_markings_per_mutcd.addItems(list_yes_no)

        self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a.addItems(list_yes_no)

        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_sidewalks_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_sidewalks_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4 = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4 = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post.addItems(list_yes_no_na)

        self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present.addItems(list_yes_no)

        self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present = qtw.QComboBox()
        self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present.addItems(list_yes_no)

        # GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        #Group TextEdits
        self.textEdit_gcws_warrants_comments = qtw.QTextEdit()
        
        # Group Labels
        self.label_gcws_warrant_private_9_3 = qtw.QLabel()
        self.label_gcws_warrant_private_9_3_1 = qtw.QLabel()
        self.label_gcws_warrant_private_9_3_2_a = qtw.QLabel()
        self.label_gcws_warrant_private_9_3_2_b = qtw.QLabel()
        self.label_gcws_warrant_private_9_3_2_c = qtw.QLabel()
        self.label_gcws_warrant_public_9_1 = qtw.QLabel()
        self.label_gcws_warrant_public_9_1_a = qtw.QLabel()
        self.label_gcws_warrant_public_9_1_b = qtw.QLabel()
        self.label_gcws_warrant_public_9_1_c = qtw.QLabel()
        self.label_gcws_warrant_public_9_1_d_i = qtw.QLabel()
        self.label_gcws_warrant_public_9_1_d_ii = qtw.QLabel()
        self.label_gcws_warrant_public_9_1_d_iii = qtw.QLabel()
        self.label_gcws_warrant_sidewalk_9_5 = qtw.QLabel()
        self.label_gates_gcws_warrant_private_9_4_1_a = qtw.QLabel()
        self.label_gates_gcws_warrant_private_9_4_1_b = qtw.QLabel()
        self.label_gates_gcws_warrant_private_9_4_1_c = qtw.QLabel()
        self.label_gates_gcws_warrant_public_9_2_1_a = qtw.QLabel()
        self.label_gates_gcws_warrant_public_9_2_1_b = qtw.QLabel()
        self.label_gates_gcws_warrant_public_9_2_1_c = qtw.QLabel()
        self.label_gates_gcws_warrant_public_9_2_1_d = qtw.QLabel()
        self.label_gates_gcws_warrant_public_9_2_1_e = qtw.QLabel()
        self.label_gates_gcws_warrant_sidewalk_9_6 = qtw.QLabel()

        # GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        #Group TextEdits
        self.textEdit_gcws_comments = qtw.QTextEdit()
         
        #Group DoubleSpinBox
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gcws_rail_crossing_warning_time_actual = qtw.QDoubleSpinBox () 

        #Group ComboBox
        self.comboBox_gcws_observe_bell_if_sidewalk = qtw.QComboBox()
        self.comboBox_gcws_observe_bell_if_sidewalk.addItems(list_yes_no)

        self.comboBox_gcws_observe_bells_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_condition.addItems(list_condition)

        self.comboBox_gcws_observe_bells_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_bells_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_bells_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_cantilever_lights_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_condition.addItems(list_condition)

        self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gates_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_condition.addItems(list_condition)

        self.comboBox_gcws_observe_gates_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gates_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_gates_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly = qtw.QComboBox()
        self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly.addItems(list_yes_no_na)

        self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly = qtw.QComboBox()
        self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly.addItems(list_yes_no_na)

        self.comboBox_gcws_observe_light_units_condition = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_condition.addItems(list_condition)

        self.comboBox_gcws_observe_light_units_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_light_units_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gcws_observe_light_units_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_gcws_observe_warning_time_consistency = qtw.QComboBox()
        self.comboBox_gcws_observe_warning_time_consistency.addItems(list_yes_no_na)
        
        self.comboBox_gcws_observe_warning_time_consistency_reduced_speed = qtw.QComboBox()
        self.comboBox_gcws_observe_warning_time_consistency_reduced_speed.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_cut_out_circuit_requirements = qtw.QComboBox()
        self.comboBox_gcws_rail_cut_out_circuit_requirements.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_directional_stick_circuit_requirements = qtw.QComboBox()
        self.comboBox_gcws_rail_directional_stick_circuit_requirements.addItems(list_yes_no_na)

        self.comboBox_gcws_rail_self_diagnostic = qtw.QComboBox()
        self.comboBox_gcws_rail_self_diagnostic.addItems(list_yes_no_na)

        #Group Labels
        self.label_gcws_rail_design_approach_warning_time = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_adjacent_crossing = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_clearance_distance = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_departure_time_pedestrian = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_departure_time_vehicle = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_gate_arm_clearance = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_preemption = qtw.QLabel()
        self.label_gcws_rail_design_warning_time_ssd = qtw.QLabel()

        # FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        #Group TextEdits
        self.textEdit_light_units_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_n_or_e_approach_height = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_light_units_measure_s_or_w_approach_height = qtw.QDoubleSpinBox () 

        #Group ComboBoxes
        self.comboBox_light_units_observe_cantilevers_per_fig_12_3 = qtw.QComboBox()
        self.comboBox_light_units_observe_cantilevers_per_fig_12_3.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_per_fig_12_1 = qtw.QComboBox()
        self.comboBox_light_units_observe_per_fig_12_1.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_sidewalks_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_sidewalks_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_sidewalks_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_sidewalks_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach = qtw.QComboBox()
        self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach.addItems(list_yes_no_na)

        # GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        #Group TextEdits
        self.textEdit_gates_gcws_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_gates_gcws_measure_gate_ascent_time = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gates_gcws_measure_gate_descent_time = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design = qtw.QDoubleSpinBox () 

        #Group DoubleSpinBox
        self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach = qtw.QDoubleSpinBox () 

        #Group Labels
        self.label_gates_gcws_calculate_gate_arm_clearance_time_recommended = qtw.QLabel()
        self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended = qtw.QLabel()

        #Group ComboBoxes
        self.comboBox_gates_gcws_observe_gate_arm_rest = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_arm_rest.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_ascent_time = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_ascent_time.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_descent_time = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_descent_time.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach.addItems(list_yes_no_na)

        self.comboBox_gates_gcws_observe_per_fig_12_2 = qtw.QComboBox()
        self.comboBox_gates_gcws_observe_per_fig_12_2.addItems(list_yes_no_na)

        # PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        #Group Text Edits
        self.textEdit_aawd_comments = qtw.QTextEdit()

        #Group DoubleSpinBox
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual = qtw.QDoubleSpinBox () 
        self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual = qtw.QDoubleSpinBox () 

        #Group ComboBoxes
        self.comboBox_aawd_observe_present_n_or_e_approach = qtw.QComboBox()
        self.comboBox_aawd_observe_present_n_or_e_approach.addItems(list_yes_no)

        self.comboBox_aawd_observe_present_s_or_w_approach = qtw.QComboBox()
        self.comboBox_aawd_observe_present_s_or_w_approach.addItems(list_yes_no)

        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach.addItems(list_yes_no_na)

        self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach = qtw.QComboBox()
        self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach.addItems(list_yes_no_na)

        #Group Labels
        self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach = qtw.QLabel()
        self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach = qtw.QLabel()
        self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended = qtw.QLabel()
        self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended = qtw.QLabel()
        self.label_aawd_warrant_gcr_lookup_road_classification = qtw.QLabel()
        self.label_aawd_warrant_gcr_observe_environmental_condition = qtw.QLabel()
        self.label_aawd_warrant_gcr_observe_sightline_obstruction = qtw.QLabel()
        self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr = qtw.QLabel()
        self.label_aawd_warrant_mutcd_lookup_significant_road_downgrade = qtw.QLabel()

        # INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        #Group TextEdits
        self.textEdit_preemption_of_traffic_signals_comments = qtw.QTextEdit()
    
        #Group LineEdits
        self.lineEdit_preemption_of_traffic_signals_road_preemption_warning_time_actual = qtw.QLineEdit() 
        self.lineEdit_preemption_of_traffic_signals_road_preemption_warning_time_design = qtw.QLineEdit() 

        #Group CombBoxes
        self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_queuing_condition = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_queuing_condition.addItems(list_yes_no)

        self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals.addItems(list_yes_no_na)

        self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type = qtw.QComboBox()
        self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type.addItems(list_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)

        #Group DatePicker
        #TODO self.label_preemption_of_traffic_signals_road_date_Last_preemption_check = pass

        #Group Labels
        self.label_preemption_of_traffic_signals_lookup_proximity_condition = qtw.QLabel()
        self.label_preemption_of_traffic_signals_lookup_required = qtw.QLabel()

        # WHISTLE CESSATION (GCS SECTION Appendix D)
        #Group TextEdits
        self.textEdit_areas_without_train_whistling_comments = qtw.QTextEdit()

        #Group ComboBoxes
        self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed.addItems(list_yes_no_na)

        self.comboBox_areas_without_train_whistling_observe_trespassing_area = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_observe_trespassing_area.addItems(list_yes_no)

        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone.addItems(list_yes_no)

        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs = qtw.QComboBox()
        self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs.addItems(list_yes_no)

        #Group Labels
        self.label_areas_without_train_whistling_lookup_gcs_12_to_16 = qtw.QLabel()
        self.label_areas_without_train_whistling_lookup_gcs_9_2 = qtw.QLabel()
        self.label_areas_without_train_whistling_requirements_observe_table_D1 = qtw.QLabel()
        

        ##################
        # Layout Objects #
        ##################
        main_layout = qtw.QGridLayout()
        toolbox = qtw.QToolBox()
        self.setLayout(main_layout)
        main_layout.addWidget(toolbox, 0, 0)

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

        # QWidgets - Create a container widget
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

        #QFormLayout - Create a form layout
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

        #Set Form Layouts to Container Widgets
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

        #Add Container Widgets to Toolbox
        toolbox.addItem(container_inspection_details, 'INSPECTION DETAILS')
        toolbox.addItem(container_collision_history, 'COLLISION HISTORY (5 YEAR PERIOD)')
        toolbox.addItem(container_general_information, 'GENERAL INFORMATION')
        toolbox.addItem(container_design_considerations, 'DESIGN CONSIDERATIONS (GCS SECTION 10)')
        toolbox.addItem(container_location_of_crossing, 'LOCATION OF GRADE CROSSING (GCS SECTION 11)')
        toolbox.addItem(container_crossing_surface, 'CROSSING SURFACE (GCS SECTION 5)')
        toolbox.addItem(container_road_geometry, 'ROAD GEOMETRY (GCS SECTION 6)')
        toolbox.addItem(container_sightlines, 'SIGHTLINES (GCS SECTION 7)')
        toolbox.addItem(container_signs_and_pavement_markings, 'SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)')
        toolbox.addItem(container_gcws_warrants, 'GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)')
        toolbox.addItem(container_gcws, 'GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)')
        toolbox.addItem(container_gcws_lights, 'FLASHING LIGHT UNITS (GCS SECTION 13 & 14)')
        toolbox.addItem(container_gcws_gates, 'GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)')
        toolbox.addItem(container_aaws, 'PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)')
        toolbox.addItem(container_interconnection_traffic_signals, 'INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)')
        toolbox.addItem(container_whistle_cessation, 'WHISTLE CESSATION (GCS SECTION Appendix D)')

        toolbox.setCurrentIndex(1)
        toolbox.setStyleSheet(styleSheet)
        
        # layout container widgets - INSPECTION DETAILS
        #TODO form_layout_inspection_details.addRow('Date of Assessment:', self.label_inspection_details_date_assessment)
        form_layout_inspection_details.addRow('Assessment Team Members & Affiliations:', self.textEdit_inspection_details_assessment_team)
        form_layout_inspection_details.addRow('Reason for Assessment:', self.comboBox_inspection_details_reason_for_assessment)
        form_layout_inspection_details.addRow('Railway Authority:', self.comboBox_inspection_details_railway_authority)
        form_layout_inspection_details.addRow('Crossing Location:', self.lineEdit_inspection_details_crossing_location)
        form_layout_inspection_details.addRow('Location Number:', self.lineEdit_inspection_details_location_number)
        form_layout_inspection_details.addRow('Subdivision Name:', self.comboBox_inspection_details_subdivision_name)
        form_layout_inspection_details.addRow('Subdivision Mile:', self.doubleSpinBox_inspection_details_subdivision_mile)
        form_layout_inspection_details.addRow('Spur Name:', self.lineEdit_inspection_details_spur_name)
        form_layout_inspection_details.addRow('Spur Mile:', self.doubleSpinBox_inspection_details_spur_mile)
        form_layout_inspection_details.addRow('Type of Crossing:', self.comboBox_inspection_details_grade_crossing_type)     
        form_layout_inspection_details.addRow('Type of Protection:', self.comboBox_inspection_details_gcws_type)
        form_layout_inspection_details.addRow('Track Type:', self.comboBox_inspection_details_track_type)
        form_layout_inspection_details.addRow('Road Authority:', self.comboBox_inspection_details_road_authority)
        form_layout_inspection_details.addRow('Municipality:', self.lineEdit_inspection_details_municipality)
        form_layout_inspection_details.addRow('Road Name:', self.lineEdit_inspection_details_road_name)   
        form_layout_inspection_details.addRow('Road Number:', self.lineEdit_inspection_details_road_number)
        form_layout_inspection_details.addRow('Province:', self.comboBox_inspection_details_province)     
        form_layout_inspection_details.addRow('Latitude:', self.doubleSpinBox_inspection_details_latitude)
        form_layout_inspection_details.addRow('Longitude:', self.doubleSpinBox_inspection_details_longitude)

        # layout container widgets - COLLISION HISTORY (5 YEAR PERIOD)
        form_layout_collision_history.addRow('Property Damage Collisions:', self.spinBox_collision_history_property_damage)
        form_layout_collision_history.addRow('Personal Injury Collisions:', self.spinBox_collision_history_personal_injury)
        form_layout_collision_history.addRow('Fatal Injury Collisions:', self.spinBox_collision_history_fatal_injury)
        form_layout_collision_history.addRow('Total Collisions in the last 5 year period:', self.label_collision_history_total_5_year_period)
        form_layout_collision_history.addRow('Number of Persons Injured:', self.spinBox_collision_history_fatalities)
        form_layout_collision_history.addRow('Number of Persons Killed:', self.spinBox_collision_history_personal_injuries)
        form_layout_collision_history.addRow('Details of Collisions:', self.textEdit_collision_history_comments)

        # layout container widgets - GENERAL INFORMATION
        form_layout_gcws_warrants.addRow(qtw.QLabel('Railway Speed'))
        form_layout_general_information.addRow('Maximum Freight Railway Operating Speed (mph)', self.spinBox_general_info_rail_max_railway_operating_speed_freight)
        form_layout_general_information.addRow('Maximum Passenger Railway Operating Speed (mph)', self.spinBox_general_info_rail_max_railway_operating_speed_passenger)
        form_layout_general_information.addRow('Railway Design Speed, VT (mph)', self.spinBox_general_info_rail_railway_design_speed)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Average Daily Train Volume'))
        form_layout_general_information.addRow('Freight Trains/Day:', self.spinBox_general_info_rail_no_trains_per_day_freight)
        form_layout_general_information.addRow('Passenger Trains/Day:', self.spinBox_general_info_rail_no_trains_per_day_passengers)
        form_layout_general_information.addRow('Total Trains/Day:', self.label_general_info_rail_no_trains_per_day_total)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Type and Number of Tracks'))
        form_layout_general_information.addRow('Main', self.spinBox_general_info_rail_no_tracks_main)
        form_layout_general_information.addRow('Other', self.spinBox_general_info_rail_no_tracks_other)
        form_layout_general_information.addRow('Number of Tracks', self.label_general_info_rail_no_tracks_total)
        form_layout_general_information.addRow('Train Switching within Crossing Approaches?', self.comboBox_general_info_rail_train_switching)
        form_layout_general_information.addRow('Road Crossing Design Speed (km/hr)', self.spinBox_general_info_road_speed_design)
        form_layout_general_information.addRow('Road Posted Speed (km/hr)', self.spinBox_general_info_road_speed_posted)
        form_layout_general_information.addRow('Current Average Annual Daily Traffic, AADT', self.spinBox_general_info_road_aadt_current)
        form_layout_general_information.addRow('Year of Count:', self.spinBox_general_info_road_aadt_year_current)
        form_layout_general_information.addRow('Forecasted Average Annual Daily Traffic, AADT', self.spinBox_general_info_road_aadt_forecast)
        form_layout_general_information.addRow('Forecast Year:', self.spinBox_general_info_road_aadt_year_forecasted)
        form_layout_general_information.addRow('Pedestrian Volume per Day', self.spinBox_general_info_road_pedestrians_per_day)
        form_layout_general_information.addRow('Cyclist Volume per Day', self.spinBox_general_info_road_cyclist_per_day)
        form_layout_general_information.addRow('Northbound / Eastbound', self.spinBox_general_info_road_no_traffic_lanes_northbound_or_eastbound)
        form_layout_general_information.addRow('Southbound / Westbound', self.spinBox_general_info_road_no_traffic_lanes_southbound_or_westbound)
        form_layout_general_information.addRow('Bidirectional', self.spinBox_general_info_road_no_traffic_lanes_bidirectional)
        form_layout_general_information.addRow('Total', self.label_general_info_road_no_traffic_lanes_total)
        form_layout_general_information.addRow('Does Grade Crossing Include sidewalk, Path, or Trail?', self.comboBox_general_info_road_sidewalks)
        form_layout_general_information.addRow('Regular Use of Crossing by Persons with Assistive Devices?', self.comboBox_general_info_road_assistive_pedestrian_devices)
        form_layout_general_information.addRow('High Seasonal Fluctuation in Volumes?', self.comboBox_general_info_road_seasonal_volume_fluctuations)
        form_layout_general_information.addRow('Is Crossing on a School Bus Route?', self.comboBox_general_info_road_school_bus_route)
        form_layout_general_information.addRow('Do Dangerous Goods Trucks Use this Roadway?', self.comboBox_general_info_road_dangerous_goods_route)
        form_layout_general_information.addRow('Other Special Road Users?', self.lineEdit_general_info_road_other_users)
        form_layout_general_information.addRow('Volume', self.spinBox_general_info_road_other_users_daily_users)
        form_layout_general_information.addRow('Surrounding Land Use:', self.comboBox_general_info_observe_surrounding_land_use)
        form_layout_general_information.addRow('Any schools, retirement homes, etc. nearby?', self.lineEdit_general_info_observe_special_buildings)
        form_layout_general_information.addRow('Urban/rural?', self.comboBox_general_info_road_classification)
        form_layout_general_information.addRow('roadway Illumination?', self.comboBox_general_info_observe_roadway_illumination)
        form_layout_general_information.addRow('Comments Regarding General Information', self.textEdit_general_info_comments)

        # layout container widgets - DESIGN CONSIDERATIONS (GCS SECTION 10)
        form_layout_design_considerations.addRow('Design Vehicle Type:', self.comboBox_design_road_design_vehicle_type)
        form_layout_design_considerations.addRow('Design Vehicle Class:', self.label_design_lookup_design_vehicle_class)
        form_layout_design_considerations.addRow('Design Vehicle Length (m):', self.label_design_lookup_design_vehicle_length)
        form_layout_design_considerations.addRow('Clearance Distance - Vehicle, cd (m):', self.doubleSpinBox_design_measure_clearance_distance_vehicle)
        form_layout_design_considerations.addRow('Vehicle Travel Distance, S = L + cd (m):', self.label_design_calculate_vehicle_travel_distance)
        form_layout_design_considerations.addRow('Departure Time - Vehicle, Td = J + T:', self.label_design_calculate_clearance_time_crossing_vehicle_design_check)
        form_layout_design_considerations.addRow("Driver's Reaction Time (s):", self.label_design_input_reaction_time)
        form_layout_design_considerations.addRow('Maximum Road Approach Grade within S (%):', self.doubleSpinBox_design_road_max_approach_grade_within_s)
        form_layout_design_considerations.addRow('Grade Adjustment Factor:', self.label_design_lookup_grade_adjustment_factor)
        form_layout_design_considerations.addRow('Do Field Acceleration Times Exceed Td?:', self.comboBox_design_observe_field_acceleration_times_exceed_td)
        form_layout_design_considerations.addRow('Clearance Distance - Pedestrian, cd (m):', self.doubleSpinBox_design_measure_clearance_distance_pedestrian)
        form_layout_design_considerations.addRow('Departure Time - Pedestrian, Td = J + T:', self.label_design_calculate_clearance_time_crossing_pedestrian_design_check)
        form_layout_design_considerations.addRow('Separation Distnace Between Adjacent Tracks (m):', self.doubleSpinBox_design_measure_adjacent_track_separation_distance)      
        form_layout_design_considerations.addRow('Adjacent Track Clearance Distance (m):', self.doubleSpinBox_design_measure_adjacent_track_clearance_distance)
        form_layout_design_considerations.addRow('Adjacent Track Clearance Time (s):', self.label_design_calculate_adjacent_track_clearance_time)
        form_layout_design_considerations.addRow('', self.label_design_calculate_clearance_time_gate_arm_ssd)
        form_layout_design_considerations.addRow('', self.label_design_calculate_clearance_time_gate_arm_stop)
        form_layout_design_considerations.addRow('', self.label_design_lookup_vehicle_departure_time_crossing)
        form_layout_design_considerations.addRow('', self.label_design_lookup_vehicle_departure_time_gate_arm_clearance)        
        form_layout_design_considerations.addRow('Design Consideration Comments', self.textEdit_design_comments)

        # layout container widgets - LOCATION OF GRADE CROSSING (GCS SECTION 11)
        form_layout_gcws_warrants.addRow(qtw.QLabel('D (Intersection with Stop Sign)'))
        form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_n_or_e_approach)
        form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_stop_s_of_w_approach)
        form_layout_gcws_warrants.addRow(qtw.QLabel('D (Signalized Intersection)'))
        form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_n_or_e_approach)
        form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_signalized_s_of_w_approach)
        form_layout_gcws_warrants.addRow(qtw.QLabel('D (Other Intersection / Driveway / Crosswalk)'))
        form_layout_location_of_crossing.addRow('N or E Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_n_or_e_approach)
        form_layout_location_of_crossing.addRow('S or W Road Approach (m):', self.doubleSpinBox_location_of_grade_crossing_nearest_intersection_other_s_of_w_approach)        
        form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles might queue onto the tracks?:', self.comboBox_location_of_grade_crossing_queue_condition)
        form_layout_location_of_crossing.addRow('Is D insufficient such that road vehicles turning from a side street might not see warning devices for the crossing?:', self.comboBox_location_of_grade_crossing_visibility_of_warning_lights)
        form_layout_location_of_crossing.addRow('Are there pedestrian crossings on either road approach that could cause vehicles to queue back to the tracks?:', self.comboBox_location_of_grade_crossing_observe_nearby_pedestrian_crosswalk)
        form_layout_location_of_crossing.addRow('Location of Grade Crossing Comments:', self.textEdit_location_of_grade_crossing_comments)

        # layout container widgets - GRADE CROSSING SURFACE (GCS SECTION 5)
        form_layout_crossing_surface.addRow('Is the crossing smooth enough to allow road vehicles, pedestrians, cyclists, and other road users to cross at their normal speed without consequence? Comments below.', self.comboBox_grade_crossing_surface_observe_crossing_smoothness)
        form_layout_crossing_surface.addRow('Grade Crossing Surface Material', self.comboBox_grade_crossing_surface_observe_material)
        form_layout_crossing_surface.addRow('Grade Crossing Surface Condition', self.comboBox_grade_crossing_surface_observe_crossing_surface_condition)
        form_layout_crossing_surface.addRow('Road Approach Surface Type', self.comboBox_grade_crossing_surface_observe_road_approach_surface_type)
        form_layout_crossing_surface.addRow('Road Approach Surface Condition', self.comboBox_grade_crossing_surface_observe_road_approach_surface_condition)        
        form_layout_crossing_surface.addRow('Crossing Surface Width (m):', self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_width)
        form_layout_crossing_surface.addRow('Centre Lane/Median Width (m):', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_median_width)
        form_layout_crossing_surface.addRow(qtw.QLabel('Travelled Way Width (m):'))
        form_layout_crossing_surface.addRow('N or E Road Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Road Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_travel_lanes_width_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Paved Shoulder Width (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_road_surface_shoulder_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Surface Extension beyond Travel Lanes/Shoulder (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_crossing_surface_extension_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Sidewalk / Path / Trail Width (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_width_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Surface Extension beyond Sidewalk / Path / Trail (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_sidewalk_extension_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Distance Between Travel Lane / Shoulder and Sidewalk / Path / Trail (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_travel_lane_and_sidewalk_s_or_w_approach)
        form_layout_crossing_surface.addRow(qtw.QLabel('Distance from path centreline to crossing warning device (m):'))
        form_layout_crossing_surface.addRow('N or E Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_n_or_e_approach)
        form_layout_crossing_surface.addRow('S or W Rail Approach:', self.doubleSpinBox_grade_crossing_surface_measure_distance_between_signal_mast_and_sidewalk_s_or_w_approach)
        form_layout_crossing_surface.addRow('Flangeway Depth (mm):', self.doubleSpinBox_grade_crossing_surface_measure_flangeway_depth)
        form_layout_crossing_surface.addRow('Flangeway Width (mm):', self.doubleSpinBox_grade_crossing_surface_measure_flangeway_width)
        form_layout_crossing_surface.addRow('Field Side Grinding Depth (mm):', self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_depth)
        form_layout_crossing_surface.addRow('Field Side Grinding Width (mm):', self.doubleSpinBox_grade_crossing_surface_measure_side_grinding_width)
        form_layout_crossing_surface.addRow('Elevation of top of Rail Above Road Surface (mm):', self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_above_road_surface)
        form_layout_crossing_surface.addRow('Elevation of top of Rail Below Road Surface (mm):', self.doubleSpinBox_grade_crossing_surface_measure_elevation_top_of_rail_below_road_surface)
        form_layout_crossing_surface.addRow('Crossing Surface Comments:', self.textEdit_grade_crossing_surface_comments)

        # layout container widgets - ROAD GEOMETRY (GCS SECTION 6)
        form_layout_road_geometry.addRow(qtw.QLabel('Are the horizontal and vertical alignments smooth and continuous throughout SSD?'))
        form_layout_road_geometry.addRow('N or E Road Approach:', self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_n_or_e_approach)
        form_layout_road_geometry.addRow('S or W Road Approach:', self.comboBox_road_geometry_observe_smooth_alignment_within_ssd_s_or_w_approach)
        form_layout_road_geometry.addRow(qtw.QLabel('Are the road lanes and shoulders at least the same width on the crossing as on the road approaches?'))
        form_layout_road_geometry.addRow('N or E Road Approach:', self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_n_or_e_approach)
        form_layout_road_geometry.addRow('S or W Road Approach:', self.comboBox_road_geometry_observe_lane_width_crossing_vs_approach_s_or_w_approach)
        form_layout_road_geometry.addRow(qtw.QLabel('Road Approach Grades (%):'))
        form_layout_road_geometry.addRow('Within 8m (N or E Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_n_or_e_approach)
        form_layout_road_geometry.addRow('Within 8m (S or W Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_8m_nearest_rail_s_or_w_approach)
        form_layout_road_geometry.addRow('Between 8m to 18m (N or E Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_n_or_e_approach)
        form_layout_road_geometry.addRow('Between 8m to 18m (S or W Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_between_8m_and_18m_nearest_rail_s_or_w_approach)
        form_layout_road_geometry.addRow('Across SSD (N or E Road Approach):', self.doubleSpinBox_road_geometry_road_general_approach_grade_n_or_e_approach)
        form_layout_road_geometry.addRow('Across SSD (S or W Road Approach):', self.doubleSpinBox_road_geometry_road_general_approach_grade_s_or_w_approach)
        form_layout_road_geometry.addRow('Within 5m of Sidewalk/Path/Trail (N or E Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_n_or_e_approach)
        form_layout_road_geometry.addRow('Within 5m of Sidewalk/Path/Trail (S or W Road Approach):', self.doubleSpinBox_road_geometry_measure_slope_within_5m_nearest_rail_at_sidewalk_s_or_w_approach)
        #form_layout_road_geometry.addRow('Allowable difference between roadway gradient and railway cross-slope (%)', self.label_road_geometry_lookup_gradient_difference)
        form_layout_road_geometry.addRow('Railway Cross Slope (%):', self.doubleSpinBox_road_geometry_measure_railway_cross_slope)
        form_layout_road_geometry.addRow('Are rail tracks super elevated? (N or E Road Approach):', self.doubleSpinBox_road_geometry_rail_superelevation_n_or_e_approach)
        form_layout_road_geometry.addRow('Are rail tracks super elevated? (S or W Road Approach):', self.doubleSpinBox_road_geometry_rail_superelevation_s_or_w_approach)
        form_layout_road_geometry.addRow('Is there any evidence that "low-bed" trucks have difficulty negotiating the crossing? (i.e. might they bottom-out or get stuck?)', self.comboBox_road_geometry_observe_low_bed_truck_condition)
        form_layout_road_geometry.addRow('Grade Crossing Angle:', self.spinBox_road_geometry_road_crossing_angle)
        form_layout_road_geometry.addRow('Road Geometry Comments:', self.textEdit_road_geometry_comments)

        # layout container widgets - SIGHTLINES (GCS SECTION 7)
        form_layout_sightlines.addRow('SSD Minimum (N or E Road Approach) (m):', self.label_sightlines_lookup_ssd_minimum_n_or_e_approach)
        form_layout_sightlines.addRow('SSD Minimum (S or W Road Approach) (m):', self.label_sightlines_lookup_ssd_minimum_s_or_w_approach)
        form_layout_sightlines.addRow('SSD Actual (N or E Road Approach) (m):', self.doubleSpinBox_sightlines_measure_ssd_actual_n_or_e_approach)
        form_layout_sightlines.addRow('SSD Actual (S or W Road Approach) (m):', self.doubleSpinBox_sightlines_measure_ssd_actual_s_or_w_approach)
        form_layout_sightlines.addRow('DSSD Minimum (ft):', self.label_sightlines_calculate_dssd_vehicle_min_ft)
        form_layout_sightlines.addRow('DSSD Minimum (m):', self.label_sightlines_calculate_dssd_vehicle_min_m)
        form_layout_sightlines.addRow("DSSD Actual (N or E Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_left)
        form_layout_sightlines.addRow("DSSD Actual (N or E Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_n_or_e_approach_right)
        form_layout_sightlines.addRow("DSSD Actual (S or W Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_left)
        form_layout_sightlines.addRow("DSSD Actual (S or W Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dssd_actual_s_or_w_approach_right)
        form_layout_sightlines.addRow('DStopped Minimum (Vehicle) (ft):', self.label_sightlines_calculate_dstopped_vehicle_min_ft)
        form_layout_sightlines.addRow('DStopped Minimum (Vehicle) (m):', self.label_sightlines_calculate_dstopped_vehicle_min_m)
        form_layout_sightlines.addRow('DStopped Minimum (Pedestiran) (ft):', self.label_sightlines_calculate_dstopped_pedestrian_min_ft)
        form_layout_sightlines.addRow('DStopped Minimum (Pedestrian) (m):', self.label_sightlines_calculate_dstopped_pedestrian_min_m)
        form_layout_sightlines.addRow("DStopped Actual (N or E Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_left)
        form_layout_sightlines.addRow("DStopped Actual (N or E Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_n_or_e_approach_driver_right)
        form_layout_sightlines.addRow("DStopped Actual (S or W Road Approach) (Driver's Left) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_left)
        form_layout_sightlines.addRow("DStopped Actual (S or W Road Approach) (Driver's Right) (m):", self.doubleSpinBox_sightlines_measure_dstopped_actual_s_or_w_approach_driver_right)
        form_layout_sightlines.addRow("Are there any obstacles within the sight triangles that affect visibility?", self.comboBox_sightlines_observe_sightline_obstructions)
        form_layout_sightlines.addRow(qtw.QLabel("Examples: Building(s), Rail/Road Alignment, Commercial Signing, Unattended Railway Equipment, Topography, Traffic Control Devices, Utilities, Vegetation)"))
        form_layout_sightlines.addRow('Sightline Comments', self.textEdit_sightlines_comments)

        # layout container widgets - SIGNS AND PAVEMENT MARKINGS (GCS SECTION 8)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_advisory_speed_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_n_or_e_approach_with_wa_18_20)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_advisory_speed_s_or_w_approach_with_wa_18_20)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_dividing_lines_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_emergency_notification_comments
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_condition)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_legible)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_condition)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_legible)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_emergency_notification_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_number_of_tracks_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_1b)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_per_fig_8_3c)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_1b)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_per_fig_8_3c)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_number_of_tracks_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_per_mutcd)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_posted_speed_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_posted_speed_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_railway_crossing_ahead_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_distance_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_distance_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_orientation)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_ahead_s_or_w_approach_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_railway_crossing_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_per_fig_8_1a)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_per_fig_8_1a)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_railway_crossing_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_sidewalks_present)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_stop_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_n_or_e_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_n_or_e_approach_per_fig_8_4)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_n_or_e_approach_same_post)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_s_or_w_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_s_or_w_approach_per_fig_8_4)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_s_or_w_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_s_or_w_approach_same_post)
        #DELETE form_layout_signs_and_pavement_markings.addRow('', self.label_signs_and_markings_stop_sign_ahead_comments)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_sign_ahead_n_or_e_approach_present)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_height)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_rail)
        form_layout_signs_and_pavement_markings.addRow('', self.doubleSpinBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_location_from_road)
        form_layout_signs_and_pavement_markings.addRow('', self.comboBox_signs_and_markings_stop_sign_ahead_s_or_w_approach_present)

        # layout container widgets - GRADE CROSSING WARNING SYSTEM WARRANTS (GCS SECTION 9)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Public Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If any of A through D below are met, then a warning system without gates is required'))
        form_layout_gcws_warrants.addRow("A. Where the forecast cross-product is 2,000 or more:", self.label_gcws_warrant_public_9_1_a)
        form_layout_gcws_warrants.addRow("B. Where there is no sidewalk, path or trail and the railway design speed is more than 129 km/hr (80 mph);", self.label_gcws_warrant_public_9_1_b)
        form_layout_gcws_warrants.addRow("C. Where there is a sidewalk, path or trail and the railway design speed is more than 81 km/hr (50 mph);", self.label_gcws_warrant_public_9_1_c)
        form_layout_gcws_warrants.addRow(qtw.QLabel('D. Where the railway design speed is more than 25 km/hr (15 mph) but less than the railway design speed referred to in (b) or (c), and'))
        form_layout_gcws_warrants.addRow("D1. Where there are two or more lines of railway where railway equipment may pass each other;", self.label_gcws_warrant_public_9_1_d_i)
        form_layout_gcws_warrants.addRow("D2. The distance as shown in Figure 9-1(a) between a Stop sign at an intersection and the nearest rail in the crossing surface is less than 30m;", self.label_gcws_warrant_public_9_1_d_ii)
        form_layout_gcws_warrants.addRow("D3. In the case of an intersection with a traffic signal, the distance between the stop line of the intersection and the nearest rail in the crossing surface, as shown in Figure 9-1(b), is less than 60m, or where there is no stop line, the distance between the travelled way and the nearest rail in the crossing surface is less than 60m.", self.label_gcws_warrant_public_9_1_d_iii)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Private Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If any of A through B below are met, then a warning system without gates is required'))
        form_layout_gcws_warrants.addRow("A. Where the forecast cross-product is 2,000 or more;", self.label_gcws_warrant_private_9_3_1)
        form_layout_gcws_warrants.addRow(qtw.QLabel('B. Where the railway design speed is more than 25 km/hr (15mph), and;'))
        form_layout_gcws_warrants.addRow("B1. The forecast cross-product is 100 or more and there are two or more lines of railway where railway equipment may pass each other;", self.label_gcws_warrant_private_9_3_2_a)
        form_layout_gcws_warrants.addRow("B2. The forecast cross-product is 100 or more and grade crossing does not include a sidewalk, path or trail and the railway design speed is more than 129 km/hr (80mph);", self.label_gcws_warrant_private_9_3_2_b)
        form_layout_gcws_warrants.addRow("B3. The grade crossing does includes a sidewalk, path or trail and the railway design speed is more than 81 km/hr (50mph);", self.label_gcws_warrant_private_9_3_2_c)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System Without Gates (Grade Crossings for a Sidewalk, Path, or Trail)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If A below is met, then a warning system without gates is required'))
        form_layout_gcws_warrants.addRow("A. The sidewalk, path or trail is outside the island circuit of an adjacent warning system and the railway design speed is more than 81 km/hr (50mph)", self.label_gcws_warrant_sidewalk_9_5)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Public Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If a warning system is warranted, and any of A through F are met, then gates are also required'))
        form_layout_gcws_warrants.addRow("A. A warning system is required under 9.1, and;", self.label_gcws_warrant_public_9_1)
        form_layout_gcws_warrants.addRow("B. The forecast cross-product is 50,000 or more;", self.label_gates_gcws_warrant_public_9_2_1_a)
        form_layout_gcws_warrants.addRow("C. There are two or more lines of railway where railway equipment may pass each other;", self.label_gates_gcws_warrant_public_9_2_1_b)
        form_layout_gcws_warrants.addRow("D. The railway design speed is more than 81 km/hr (50mph);", self.label_gates_gcws_warrant_public_9_2_1_c)
        form_layout_gcws_warrants.addRow("E. The distance as shown in Figure 9-1(a) between a Stop sign at an intersection and the nearest rail in the crossing surface is less than 30m;", self.label_gates_gcws_warrant_public_9_2_1_d)
        form_layout_gcws_warrants.addRow("F. In the case of an intersection with a traffic signal, the distance between the stop line of the intersection and the nearest rail in the crossing surface, as shown in Figure 9-1(b), is less than 60m, or where there is no stop line, the distance between the travelled way and the nearest rail in the crossing surface is less than 60m.", self.label_gates_gcws_warrant_public_9_2_1_e)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Private Crossings)'))
        form_layout_gcws_warrants.addRow(qtw.QLabel('If a warning system is warranted, and any of A through D are met, then gates are also required'))
        form_layout_gcws_warrants.addRow("A. A warning system is required under 9.1, and;", self.label_gcws_warrant_private_9_3)
        form_layout_gcws_warrants.addRow("B. The forecast cross-product is 50,000 or more;", self.label_gates_gcws_warrant_private_9_4_1_a)
        form_layout_gcws_warrants.addRow("C. There are two or more lines of railway where railway equipment may pass each other;", self.label_gates_gcws_warrant_private_9_4_1_b)
        form_layout_gcws_warrants.addRow("D. The railway design speed is more than 81 km/hr (50mph);", self.label_gates_gcws_warrant_private_9_4_1_c)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Warrants for a Warning System With Gates (Grade Crossings for a Sidewalk, Path, or Trail)'))
        form_layout_gcws_warrants.addRow("", self.label_gates_gcws_warrant_sidewalk_9_6)
        form_layout_gcws_warrants.addRow('GCWS Warrants Comments', self.textEdit_gcws_warrants_comments)

        # layout container widgets - GRADE CROSSING WARNING SYSTEMS (GCS SECTION 12-16)
        form_layout_gcws.addRow('Design Approach Warning Time:', self.label_gcws_rail_design_approach_warning_time)
        form_layout_gcws_warrants.addRow(qtw.QLabel('Should be greatest of:'))
        form_layout_gcws.addRow("a. 20 s, unless the grade crossing clearance distance (Fig 10-1) is more than 11 m (35 ft), in which case, the 20 s must be increased by one second for each additional 3 m (10 ft), or fraction thereof;", self.label_gcws_rail_design_warning_time_clearance_distance)
        form_layout_gcws.addRow("b. The Departure Time for the grade crossing 'design vehicle' (Article 10.3.2);", self.label_gcws_rail_design_warning_time_departure_time_vehicle)
        form_layout_gcws.addRow("c. The Departure Time for pedestrians, cyclists, and persons using assistive devices (Article 10.3.3);", self.label_gcws_rail_design_warning_time_departure_time_pedestrian)
        form_layout_gcws.addRow("d. The gate arm clearance time, plus the time to complete the gate arm descent, plus 5 seconds;", self.label_gcws_rail_design_warning_time_gate_arm_clearance)
        form_layout_gcws.addRow("e. The minimum warning time required for traffic signal pre-emption;", self.label_gcws_rail_design_warning_time_preemption)
        form_layout_gcws.addRow("f. The time for the design vehicle travelling at the design speed to travel from the stopping sight distance, as specified in article 1.2.5.2 of the Geometric Design Guide and pass completely through the clearance distance;", self.label_gcws_rail_design_warning_time_ssd)
        form_layout_gcws.addRow("g. Adjacent Track Interconnected Highway-Rail Grade Crossing. (add to (a), - (e))", self.label_gcws_rail_design_warning_time_adjacent_crossing)
        form_layout_gcws.addRow('Actual Approach Warning Time:', self.doubleSpinBox_gcws_rail_crossing_warning_time_actual)
        form_layout_gcws.addRow(qtw.QLabel("Warning Systems Clearance Distance from Railway (Min. 3.66 m (12 ft) for signal mast or 3.05 m (10 ft) for end of gate arm; from centreline of track) (m):"))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_rail)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_rail)
        form_layout_gcws.addRow(qtw.QLabel("Warning System Clearance Distance from Roadway (Min. 625 mm from curb; or 1.875 m from travelled way and 625 mm from shoulder) (m)"))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_from_road)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_from_road)
        form_layout_gcws.addRow(qtw.QLabel("Distance between top of foundation and surrounding ground level (max. 100 mm (4 in))"))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_distance_top_of_foundation)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_distance_top_of_foundation)
        form_layout_gcws.addRow(qtw.QLabel("Is the slope of surrounding ground from foundation towards the travelled way less than 25% (4:1)?"))
        form_layout_gcws.addRow('N or E Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_n_or_e_approach_slope_from_foundation)
        form_layout_gcws.addRow('S or W Road Approach:', self.doubleSpinBox_gcws_measure_warning_device_s_or_w_approach_slope_from_foundation)
        form_layout_gcws.addRow(qtw.QLabel("Light units:"))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_light_units_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_light_units_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_light_units_condition)
        form_layout_gcws.addRow(qtw.QLabel("Cantilever Lights:"))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_cantilever_lights_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_cantilever_lights_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_cantilever_lights_condition)
        form_layout_gcws.addRow('If there is only one sidewalk, is a bell located on the adjacent assembly?', self.comboBox_gcws_observe_bell_if_sidewalk)
        form_layout_gcws.addRow(qtw.QLabel("Bells:"))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_bells_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_bells_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_bells_condition)
        form_layout_gcws.addRow(qtw.QLabel("Gates:"))
        form_layout_gcws.addRow('N or E Road Approach:', self.comboBox_gcws_observe_gates_n_or_e_approach)
        form_layout_gcws.addRow('S or W Road Approach:', self.comboBox_gcws_observe_gates_s_or_w_approach)
        form_layout_gcws.addRow('Condition:', self.comboBox_gcws_observe_gates_condition)
        form_layout_gcws.addRow('Is crossing warning system equipped with monitoring devices that gather and retain the data and time of information (per 12.2) for a min. of 30 days?', self.comboBox_gcws_rail_self_diagnostic)
        form_layout_gcws.addRow('Does crossing warning system provide consitent warning times for railway equipment regularly operating over the grade crossing?', self.comboBox_gcws_observe_warning_time_consistency)
        form_layout_gcws.addRow('Where Railway Design Speed has been reduced, other than TSO, does actual Crossing Warning Time exceed 13s compared with design?', self.comboBox_gcws_observe_warning_time_consistency_reduced_speed)
        form_layout_gcws.addRow('Where railway eqipment regularly stops, left standing or turnout present within limits of warning systems, are Cut-Out Circuits in place?', self.comboBox_gcws_rail_cut_out_circuit_requirements)
        form_layout_gcws.addRow('If Directional Stick Circuits present, are requirments of GCS 16.4 met?', self.comboBox_gcws_rail_directional_stick_circuit_requirements)
        form_layout_gcws.addRow('Limited Use Warning System without Walk Light Assembly (Y/N)? (For Private Crossing with fewer than 3 residential dwellings only)', self.comboBox_gcws_observe_gcws_limited_use_without_walk_light_assembly)
        form_layout_gcws.addRow('Limited Use Warning System with Walk Light Assembly (Y/N)? (For Private Crossing and restricted access only)', self.comboBox_gcws_observe_gcws_limited_use_with_walk_light_assembly)
        form_layout_gcws.addRow('GCWS Comments', self.textEdit_gcws_comments)
        
        # layout container widgets - FLASHING LIGHT UNITS (GCS SECTION 13 & 14)
        form_layout_gcws_lights.addRow('Are signal assemblies as shown in Figure 12-1?', self.comboBox_light_units_observe_per_fig_12_1)
        form_layout_gcws_lights.addRow(qtw.QLabel('Alignment Height (m):'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.doubleSpinBox_light_units_measure_n_or_e_approach_height)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.doubleSpinBox_light_units_measure_s_or_w_approach_height)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are primary light units visible for at least the minimum SSD?'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.comboBox_light_units_observe_visibility_front_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.comboBox_light_units_observe_visibility_front_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are additional light units required to cover intermediate areas of the road approaches?'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.comboBox_light_units_observe_supplemental_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.comboBox_light_units_observe_supplemental_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are back light units visible by stopped vehicles at least 15 m?'))
        form_layout_gcws_lights.addRow('N or E Road Approach:', self.comboBox_light_units_observe_visibility_back_lights_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Road Approach:', self.comboBox_light_units_observe_visibility_back_lights_s_or_w_approach)
        form_layout_gcws_lights.addRow(qtw.QLabel('Are lights installed exclusively for sidewalks, paths or trails visible for at least 30 m?'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.comboBox_light_units_observe_sidewalks_n_or_e_approach)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.comboBox_light_units_observe_sidewalks_s_or_w_approach)
        form_layout_gcws_lights.addRow('Are cantilevers as shown in Figure 12-3?', self.comboBox_light_units_observe_cantilevers_per_fig_12_3)
        form_layout_gcws_lights.addRow(qtw.QLabel('Distance from nearest rail (m):'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_rail)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_rail)
        form_layout_gcws_lights.addRow(qtw.QLabel('Distance from travelled way (m):'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_distance_from_road)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_distance_from_road)
        form_layout_gcws_lights.addRow(qtw.QLabel('Height (m):'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_height)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_height)
        form_layout_gcws_lights.addRow(qtw.QLabel('DR (m):'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dr)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dr)
        form_layout_gcws_lights.addRow(qtw.QLabel('DL (m):'))
        form_layout_gcws_lights.addRow('N or E Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_n_or_e_approach_dl)
        form_layout_gcws_lights.addRow('S or W Rail Approach:', self.doubleSpinBox_light_units_measure_cantilevers_s_or_w_approach_dl)
        form_layout_gcws_lights.addRow('Light Unit Comments:', self.textEdit_light_units_comments)

        # layout container widgets - GATES FOR GRADE CROSSING WARNING SYSTEMS (GCS SECTION 10, 12, 15)
        form_layout_gcws_gates.addRow('Gate arm delay (Recommended) (s):', self.label_gates_gcws_calculate_gate_arm_clearance_time_recommended)
        form_layout_gcws_gates.addRow('Gate Arm Delay Time (from Plans) (s):', self.doubleSpinBox_gates_gcws_rail_gate_arm_delay_time_design)
        form_layout_gcws_gates.addRow('Gate Arm Descent Time (from Plans) (s)', self.doubleSpinBox_gates_gcws_rail_gate_arm_descent_time_design)
        form_layout_gcws_gates.addRow('Inner Gate Arm Delay Time for Adjacent Track Interconnected Highway-Rail Grade Crossing (Recommended) (s)', self.label_gates_gcws_calculate_inner_gate_arm_delay_time_recommended)
        form_layout_gcws_gates.addRow('nner Gate Arm Delay Time for Adjacent Track Interconnected Highway-Rail Grade Crossing (from Plans) (s)', self.doubleSpinBox_gates_gcws_rail_inner_gate_arm_delay_time_design)
        form_layout_gcws_gates.addRow('Measure Gate Ascent Time (Actual) (s)', self.doubleSpinBox_gates_gcws_measure_gate_ascent_time)
        form_layout_gcws_gates.addRow('Measure Gate Descent Time (Actual) (s)', self.doubleSpinBox_gates_gcws_measure_gate_descent_time)
        form_layout_gcws_gates.addRow('Check Gate Ascent Time (6 to 12 sec)', self.comboBox_gates_gcws_observe_gate_ascent_time)
        form_layout_gcws_gates.addRow('Check Gate Descent Time (10 to 15 sec)', self.comboBox_gates_gcws_observe_gate_descent_time)
        form_layout_gcws_gates.addRow('Does gate arm come to rest in the horizontal position not less than 5s before the arrival at the crossing of railway equipment?', self.comboBox_gates_gcws_observe_gate_arm_rest)
        form_layout_gcws_gates.addRow('Are gates as shown in Figure 12-2?', self.comboBox_gates_gcws_observe_per_fig_12_2)
        form_layout_gcws_gates.addRow(qtw.QLabel('Are strips on the gate arm 406 mm (16 in.) wide and aligned vertically?'))
        form_layout_gcws_gates.addRow('N or E Road Approach:', self.comboBox_gates_gcws_observe_gate_strips_n_or_e_approach)
        form_layout_gcws_gates.addRow('S or W Road Approach:', self.comboBox_gates_gcws_observe_gate_strips_s_or_w_approach)
        form_layout_gcws_gates.addRow(qtw.QLabel('Distance between the end of the gate arm and the longitudinal axis of the road approach (m):'))
        form_layout_gcws_gates.addRow('N or E Road Approach:', self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_n_or_e_approach)
        form_layout_gcws_gates.addRow('S or W Road Approach:', self.doubleSpinBox_gates_gcws_measure_distance_between_gate_end_and_road_cl_s_or_w_approach)
        form_layout_gcws_gates.addRow('Gates for GCWS Comments', self.textEdit_gates_gcws_comments)

        # layout container widgets - PREPARE TO STOP AT RAILWAY CROSSING SIGN (GCS SECTION 18)
        form_layout_aaws.addRow(qtw.QLabel('Are Prepare to Stop at Railway Crossing Sign present?'))
        form_layout_aaws.addRow('N or E Road Approach:', self.comboBox_aawd_observe_present_n_or_e_approach)
        form_layout_aaws.addRow('S or W Road Approach:', self.comboBox_aawd_observe_present_s_or_w_approach)
        form_layout_aaws.addRow(qtw.QLabel('Warrants for a Prepare to Stop at Railway Crossing Sign Per GCR'))
        form_layout_aaws.addRow('A. Is the roadway classified as an expressway?', self.label_aawd_warrant_gcr_lookup_road_classification)
        form_layout_aaws.addRow('B. Is at least one set of front lights on the warning system not clearly visible within the stopping sight distance of at least one of the lanes of the road approach?', self.label_aawd_warrant_gcr_observe_sightline_obstruction)
        form_layout_aaws.addRow('C. Do weather conditions at the grade crossing repeatedly obscure the visibility of the warning system?', self.label_aawd_warrant_gcr_observe_environmental_condition)
        form_layout_aaws.addRow(qtw.QLabel('Warrants for a Prepare to Stop at Railway Crossing Sign Per MUTCD'))
        form_layout_aaws.addRow('D. Is the speed limit of the travelled way greater than 90 km/h?', self.label_aawd_warrant_mutcd_lookup_road_speed_limit_greater_than_90_km_per_hr)
        form_layout_aaws.addRow('E. Is the crossing at the bottom of a hill or downgrade of considerable length?', self.label_aawd_warrant_mutcd_lookup_significant_road_downgrade)
        form_layout_aaws.addRow(qtw.QLabel('Design AAWD Advance Activation Time (s):'))
        form_layout_aaws.addRow('N or E Road Approach:', self.label_aawd_calculate_advance_activation_time_design_n_or_e_approach)
        form_layout_aaws.addRow('S or W Road Approach:', self.label_aawd_calculate_advance_activation_time_design_s_or_w_approach)
        form_layout_aaws.addRow(qtw.QLabel('Recommended minimum Advance Warning Flasher Distance from Railway'))
        form_layout_aaws.addRow('N or E Road Approach:', self.label_aawd_calculate_distance_sign_and_stop_n_or_e_approach_recommended)
        form_layout_aaws.addRow('S or W Road Approach:', self.label_aawd_calculate_distance_sign_and_stop_s_or_w_approach_recommended)
        form_layout_aaws.addRow(qtw.QLabel('Actual Advance Warning Flasher Distance from Railway'))
        form_layout_aaws.addRow('N or E Road Approach:', self.doubleSpinBox_aawd_measure_distance_sign_and_stop_n_or_e_approach_actual)
        form_layout_aaws.addRow('S or W Road Approach:', self.doubleSpinBox_aawd_measure_distance_sign_and_stop_s_or_w_approach_actual)
        form_layout_aaws.addRow(qtw.QLabel('Does the advance activation time provide sufficient time for a vehicle to:'))
        form_layout_aaws.addRow(qtw.QLabel('a) clear the grade crossing before the arrival of railway equipment at the crossing surface (FLB)'))
        form_layout_aaws.addRow(qtw.QLabel('b) clear the grade crossing before gate arms start to descend (FLBG)'))
        form_layout_aaws.addRow('N or E Road Approach:', self.comboBox_aawd_road_aawd_sufficient_activation_time_n_or_e_approach)
        form_layout_aaws.addRow('S or W Road Approach:', self.comboBox_aawd_road_aawd_sufficient_activation_time_s_or_w_approach)
        form_layout_aaws.addRow('Prepare to Stop at Railway Crossing Sign Comments', self.textEdit_aawd_comments)

        # layout container widgets - INTERCONNECTION OF TRAFFIC SIGNALS (GCS SECTION 19)
        form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Warrants for an Interconnected Traffic Signal'))
        form_layout_interconnection_traffic_signals.addRow('Is there less than 30m between the nearest rail of a grade crossing and the travelled way of an intersection with traffic signals?', self.label_preemption_of_traffic_signals_lookup_proximity_condition)
        form_layout_interconnection_traffic_signals.addRow('Is an Interconnected Traffic Signal required?', self.label_preemption_of_traffic_signals_lookup_required)
        form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Other Queuing Condition(s)'))
        form_layout_interconnection_traffic_signals.addRow('Is "D" insufficient such that road vehicles might queue onto the rail tracks? (I.E. less than 60 m for traffic signals; 30 m or more for a Stop sign (or 60 m or more for traffic signals) with queued traffic encroaching within 2.4 m of the nearest rail; a situation causing vehicles to routinely queue closer than 2.4 m to the nearest rail in the crossing (Example(s): Yield sign, a roundabout, a pedestrian crossing, a bikeway, or a stopped vehicle waiting to make left turn))', self.comboBox_preemption_of_traffic_signals_observe_queuing_condition)
        form_layout_interconnection_traffic_signals.addRow('Are adjacent traffic signals interconnected with a grade crossing warning system?', self.comboBox_preemption_of_traffic_signals_road_or_rail_crossing_preemption_type)
        form_layout_interconnection_traffic_signals.addRow('Design Preemption activation warning time required for traffic signal preemption (s):', self.lineEdit_preemption_of_traffic_signals_road_preemption_warning_time_design)
        form_layout_interconnection_traffic_signals.addRow('Actual Preemption activation warning time required for traffic signal preemption (s):', self.lineEdit_preemption_of_traffic_signals_road_preemption_warning_time_actual)
        form_layout_interconnection_traffic_signals.addRow(qtw.QLabel('Field checks:'))
        #form_layout_interconnection_traffic_signals.addRow('Date of last pre-emption check?', self.label_preemption_of_traffic_signals_road_date_Last_preemption_check)
        form_layout_interconnection_traffic_signals.addRow('Does interconnection provide adequate time to clear traffic from the grade crossing before the arrival of railway equipment?', self.comboBox_preemption_of_traffic_signals_observe_traffic_clearance_time_adequate)
        form_layout_interconnection_traffic_signals.addRow('Does interconnection prohibit road traffic from moving from the street intersection towards the grade crossing?', self.comboBox_preemption_of_traffic_signals_observe_unintended_queuing_by_traffic_signals)
        form_layout_interconnection_traffic_signals.addRow('Are there known queuing issues at the tracks?', self.comboBox_preemption_of_traffic_signals_observe_known_queuing_issues)
        form_layout_interconnection_traffic_signals.addRow('Are pedestrians accommodated during the pre-emption?', self.comboBox_preemption_of_traffic_signals_observe_pedestrian_accommodation)
        form_layout_interconnection_traffic_signals.addRow('Have longer/slower vehicles been considered (compared to Design Vehicle)?', self.comboBox_preemption_of_traffic_signals_observe_consideration_of_Longer_vehicles)       
        form_layout_interconnection_traffic_signals.addRow('Are supplemental signs needed for motorists (no right turn on red light, etc)?', self.comboBox_preemption_of_traffic_signals_observe_supplemental_signage)
        form_layout_interconnection_traffic_signals.addRow('Preemption of Traffic Signals Comments', self.textEdit_preemption_of_traffic_signals_comments)

        # layout container widgets - WHISTLE CESSATION (GCS SECTION Appendix D)
        form_layout_whistle_cessation.addRow('Is train whistling prohibited at this crossing?', self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone)
        form_layout_whistle_cessation.addRow('24 hours per day?', self.comboBox_areas_without_train_whistling_rail_anti_whistling_zone_24_hrs)
        form_layout_whistle_cessation.addRow(qtw.QLabel('Requirements'))
        form_layout_whistle_cessation.addRow('Is there evidence of routine unauthorized access (trespassing) on the rail line in the area of the crossing? Comment below.', self.comboBox_areas_without_train_whistling_observe_trespassing_area)
        form_layout_whistle_cessation.addRow('What is the required type of warning system as per Table D-1?', self.label_areas_without_train_whistling_requirements_observe_table_D1)
        form_layout_whistle_cessation.addRow('Further to Column A of Table D-1, is a crossing warning system with gates installed per GCS 9.2?', self.label_areas_without_train_whistling_lookup_gcs_9_2)
        form_layout_whistle_cessation.addRow('Does crossing warning system meet requirements of GCS 12-16?', self.label_areas_without_train_whistling_lookup_gcs_12_to_16)
        form_layout_whistle_cessation.addRow('If Stop and Proceed, is crossing equipped with FLB meeting GCS 12-16 or manually protected?', self.comboBox_areas_without_train_whistling_observe_for_stop_and_proceed)       
        form_layout_whistle_cessation.addRow('Whistle Cessation Comments', self.textEdit_areas_without_train_whistling_comments)


        '''
        #######################
        # Size Control Layout #
        #######################

        # use stretch factor

        stretch_layout = qtw.QHBoxLayout()
        main_layout.addLayout(stretch_layout)
        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)
        
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
        charcount_self.label = qtw.QLabel("chars: 0")
        self.textedit.textChanged.connect(
            lambda: charcount_self.label.setText(
                "chars: " +
                str(len(self.textedit.toPlainText()))
                )
            )
        self.statusBar().addPermanentWidget(charcount_self.label)

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
    