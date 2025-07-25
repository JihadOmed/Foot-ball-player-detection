from Utilites.Video_Utilites import read_video, save_video
from Tracking.Track import Tracker
from Assigning.Player_assign import TeamAssigner
from Assigning.Player_ball_assign import PlayerBallAssigner
import numpy as np
from Camera_Movement.camera_estimator import CameraMovementEstimator
from View_Transformer.View import ViewTransformer
from Speed_Distance.Estimator import SpeedAndDistance_Estimator
import cv2


def main():
    # Read Video
    video_frames = read_video('Input_Videos/Football.mp4')

    # Initialize Tracker
    tracker = Tracker('Models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                    read_from_stub=True,
                                    stub_path='stubs/track_stubs.pkl')
    # Get object positions 
    tracker.add_position_to_tracks(tracks)

    # camera movement estimator
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames,
                                                                                read_from_stub=True,
                                                                                stub_path='stubs/camera_movement_stub.pkl')
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks,camera_movement_per_frame)


    # View Trasnformer
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)

    # Interpolate Ball Positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    # Speed and distance estimator
    speed_and_distance_estimator = SpeedAndDistance_Estimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

    # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['player'][0])
    
    for frame_num, player_track in enumerate(tracks['player']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                track['bbox'],
                                                player_id)
            tracks['player'][frame_num][player_id]['team'] = team 
            tracks['player'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    
    # Assign Ball Aquisition
    player_assigner =PlayerBallAssigner()
    team_ball_control= []
    for frame_num, player_track in enumerate(tracks['player']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['player'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['player'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1])
    team_ball_control= np.array(team_ball_control)


    # Draw output 
    ## Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)

    ## Draw Camera movement
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames,camera_movement_per_frame)

    ## Draw Speed and Distance
    speed_and_distance_estimator.draw_speed_and_distance(output_video_frames,tracks)

    # Save video
    save_video(output_video_frames, 'Output_Videos/Football.avi')

if __name__ == '__main__':
    main()