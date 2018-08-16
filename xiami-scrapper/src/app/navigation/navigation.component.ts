import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {
  isLinear = true;
  ID_or_text: string;
  // playlist_info: string;
  parsed_playlist: JSON;

  constructor(
    private http: HttpClient,
  ) {}


  private xiami_parser_URL = 'http://127.0.0.1:5000/';  // URL to web api
  public playlist_ID = '353034283'; // default values
  public special_symbols = '+?';
  public playlist_info = '';


  ngOnInit() {
  }

  // Always subscribe! (Observables are lazy.)
  // An HttpClient method does not begin its HTTP request until you
  // call subscribe() on the observable returned by that method. This is true for all HttpClient methods.
  /** GET heroes from the server */
  private post_to_server() {
    delete this.parsed_playlist;
    if (this.ID_or_text === 'Playlist ID') {
      this.http.post('http://127.0.0.1:5000/xiami_ID', {playlist_ID: this.playlist_ID})
      .subscribe(
        data => {console.log(data); }
      ); } else {
        this.http.post('http://127.0.0.1:5000/xiami_info', {playlist_info: this.playlist_info, special_symbols: this.special_symbols})
      .subscribe(
        data => {console.log(data); }
      );
    }
    // alert(this.playlist_ID);
  }

  /** GET heroes from the server */
  //  subscribe is needed for observable from GET
  public get_from_server() {
    this.http.get(this.xiami_parser_URL + 'xiami_parsed_result')
    .subscribe(data => {
      this.parsed_playlist = data as JSON;
      console.log(this.parsed_playlist); });
  }

  // this is the HTTP post and HTTP get that we wrote 
  // https://angular.io/guide/template-syntax#ref-vars
  // use the #parsed-playlist as the selector for the element
  public copyInputMessage(inputElement){
    inputElement.select();
    document.execCommand('copy');
    inputElement.setSelectionRange(0, 0);
  }
}